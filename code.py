from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from TOKEN import token
import time


black = '⚫️'
white = '⚪️'

def enc(board):
    number = 0
    base = 3
    for row in range(8):
        for col in range(8):
            number *= base
            if board.get((row, col)) == black:
                number += 2
            elif board.get((row, col)) == white:
                number += 1
    return str(number)

def dec(number):
    board = {}
    base = 3
    for row in [7, 6, 5, 4, 3, 2, 1, 0]:
        for col in [7, 6, 5, 4, 3, 2, 1, 0]:
            if number % 3 == 2:
                board[(row, col)] = black
            elif number % 3 == 1:
                board[(row, col)] = white
            number //= base
    return board

def board_markup(board):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(board.get((row, col), ' '), callback_data=f'{row}{col}{enc(board)}') for col in range(8)]
        for row in range(8)])

def is_valid_move(board, color, row, col):
    if (row, col) in board:
        return False

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if (row + dx, col + dy) in board and board[(row + dx, col + dy)] != color:
                x = row + dx
                y = col + dy
                while (x, y) in board:
                    if board[(x, y)] == color:
                        return True
                    x += dx
                    y += dy

    return False

def make_move(board, color, row, col):
    board[(row, col)] = color

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if (row + dx, col + dy) in board and board[(row + dx, col + dy)] != color:
                x = row + dx
                y = col + dy
                flip_positions = []
                while (x, y) in board:
                    if board[(x, y)] == color:
                        for pos in flip_positions:
                            board[pos] = color
                        break
                    flip_positions.append((x, y))
                    x += dx
                    y += dy

def is_game_over(board):
    if len(board) == 64:
        return True

    black_moves = get_valid_moves(board, black)
    white_moves = get_valid_moves(board, white)

    return len(black_moves) == 0 and len(white_moves) == 0

def get_valid_moves(board, color):
    moves = []
    for row in range(8):
        for col in range(8):
            if is_valid_move(board, color, row, col):
                moves.append((row, col))
    return moves


async def handle_move(update, context):
    data = update.callback_query.data
    row = int(data[0])
    col = int(data[1])
    board = dec(int(data[2:]))

    if is_valid_move(board, black, row, col):
        make_move(board, black, row, col)
        await context.bot.edit_message_reply_markup(chat_id=update.callback_query.message.chat_id,
                                                message_id=update.callback_query.message.message_id,
                                                reply_markup=board_markup(board))
        if is_game_over(board):
            black_score, white_score = score(board)
            if(black_score>white_score):
                result="黑子獲勝!!"
            elif(white_score>black_score):
                result="白子獲勝!!"
            else:
                result="平局~"
            await context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                           text=f'遊戲结束！ {result}\n黑子數量：{black_score}\n白子數量：{white_score}')
            return
    else:
        await context.bot.answer_callback_query(update.callback_query.id, '此處無法下。')
        return
        
    
    time.sleep(1)
    
    while True:
        
        white_moves = get_valid_moves(board, white)

        if white_moves:
            import random
            white_row, white_col = random.choice(white_moves)
            make_move(board, white, white_row, white_col)
            await context.bot.edit_message_reply_markup(chat_id=update.callback_query.message.chat_id,
                                                    message_id=update.callback_query.message.message_id,
                                                    reply_markup=board_markup(board))
            if is_game_over(board):
                black_score, white_score = score(board)
                if(black_score>white_score):
                    result="黑子獲勝!!"
                elif(white_score>black_score):
                    result="白子獲勝!!"
                else:
                    result="平局~"
                await context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                            text=f'遊戲结束！ {result}\n黑子數量：{black_score}\n白子數量：{white_score}')
                return
        else:
            await context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                        text="白子無處可下，黑子續下")
        black_moves = get_valid_moves(board, black)
        if black_moves:    
            return
        await context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                        text="黑子無處可下，白子續下")
        

    

async def start_game(update, context):
    board = {(3, 3): black, (3, 4): white, (4, 3): white, (4, 4): black}
    await update.message.reply_text('遊戲開始！', reply_markup=board_markup(board))



def score(board):
    black_score = 0
    white_score = 0
    for piece in board.values():
        if piece == black:
            black_score += 1
        elif piece == white:
            white_score += 1
    return black_score, white_score

def main():
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start_game))
    application.add_handler(CallbackQueryHandler(handle_move))
    application.run_polling()

if __name__ == "__main__":
    main()
