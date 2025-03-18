from turtle import clear
import telegram
from telegram import Update
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram._passport.credentials import decrypt
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
import configparser

async def clear_chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = None
    first_message_id = None

    if update.message:
        chat_id = update.message.chat_id
        first_message_id = update.message.message_id - 10
    elif update.callback_query:
        chat_id = update.callback_query.message.chat_id
        first_message_id = update.callback_query.message.message_id - 10

    if chat_id is not None and first_message_id is not None:
        last_message_id = first_message_id + 10
        # uzenetek torlese tartomanyban
        for message_id in range(first_message_id, last_message_id + 1):
            try:
                await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            except:
                pass  # Ha egy uzenet nem torolheto (pl. nem letezik), akkor lepj tovabb


# uzenet torlese
async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        chat_id = update.message.chat_id
        message_id = update.message.message_id
    elif update.callback_query:
        chat_id = update.callback_query.message.chat_id
        message_id = update.callback_query.message.message_id

    await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    
async def delete_user_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        chat_id = update.message.chat_id
        message_id = update.message.message_id
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

# A parancsok kezelese
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await clear_chat(update, context)
    keyboard = [
        [InlineKeyboardButton("🎵 Music ", callback_data='music')],
        [InlineKeyboardButton("🎞️ Video Clips ", callback_data='clips')],
        [InlineKeyboardButton("▶️ Playlists ", callback_data='lists')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text('🇼 🇪 🇱 🇨 🇴 🇲 🇪 ‼️\n\nYou can find here my projects.', reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.reply_text('🇼 🇪 🇱 🇨 🇴 🇲 🇪 ‼️\n\nYou can find here my projects.', reply_markup=reply_markup)
       
async def clips(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await clear_chat(update, context)
    keyboard = [
        [InlineKeyboardButton("🏠 Home", callback_data='start')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text('Clips', reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.reply_text('Clips', reply_markup=reply_markup)
async def lists(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await clear_chat(update, context)
    keyboard = [
        [InlineKeyboardButton("🍺 Punk", callback_data='punk')],
        [InlineKeyboardButton("🏠 Home", callback_data='start')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text('Choose your style:', reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.reply_text('Choose your style:', reply_markup=reply_markup)
       
async def music(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("☣️ Decrypted Souls", callback_data='decrypted')],
        [InlineKeyboardButton("🍻 Szofistick", callback_data='szofi')], 
        [InlineKeyboardButton("🎸 Pres", callback_data='pres')],
        [InlineKeyboardButton("🏠 Home", callback_data='start')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text('🎵 🇲 🇺 🇸 🇮 🇨 🎵', reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.reply_text('🎵 🇲 🇺 🇸 🇮 🇨 🎵', reply_markup=reply_markup)
        


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    
    await query.answer()
    
    await delete(update, context)

    if query.data == 'start':
        await start(update, context)
    elif query.data == 'music':
        await music(update, context)
    elif query.data == 'lists':
        await lists(update, context)
    elif query.data == 'punk':
        await query.message.reply_text('▶️ Top Punk playlists:')
        await query.message.reply_text('1️⃣\n\nhttps://music.youtube.com/playlist?list=PLwLnzHYUoEtIsynhBPXaXVXBcgU5KY5YB&si=-nR_6iA5JxqByzuj')
        await lists(update, context)
    elif query.data == 'clips':
        await query.message.reply_text('🎞️ 🇨 🇱 🇮 🇵 🇸 🎞️')
        await query.message.reply_text('https://www.youtube.com/watch?v=ryV57amkNNc')
        await clips(update, context)
    elif query.data == 'szofi':
        await query.message.reply_text('Subscribe Szofistick on Youtube\n\nLink:\nhttps://www.youtube.com/@SuperPeety')
        await music(update, context)
    elif query.data == 'decrypted':
        await query.message.reply_text('Subscribe Decrypted Souls on Youtube\n\nLink:\nhttps://www.youtube.com/@decryptedsouls5807')
        await music(update, context)
    elif query.data == 'pres':
        await query.message.reply_text('Subscribe Pres on Youtube\n\nLink:\nhttps://www.youtube.com/@preszenekar9819')
        await music(update, context)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await delete_user_message(update, context)
    
def get_token():
    config = configparser.ConfigParser()
    config.read('api.ini')
    return config['API']['TOKEN']

def main():
    # Az API tokened
    TOKEN = get_token()

    # Bot inicializalasa az API tokennel
    application = Application.builder().token(TOKEN).build()

    # A parancsok kezelese
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("clear", clear_chat))
    

    # A bot inditasa
    application.run_polling()

if __name__ == '__main__':
    main()
