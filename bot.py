from typing import Final
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Application, filters, ContextTypes
import pyjokes

TOKEN: Final = '8406097080:AAG9KA2-TP332UQe4eEYrMkUsFR_072lh0o'
BOT_USERNAME: Final = '@llllluci_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello this is my personal BOT, I am jarvis! I know this is not the name but I will use it because this is MINE')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Please contact with my GOD! His name is Tojo')
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Jani na kothai acho tumi koto dure')
    
async def jokes_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(pyjokes.get_joke())
    

def handle_response(text: str) -> str:
    processed: str = text.lower().strip()

    if any(word in processed for word in ['hi', 'hello', 'helo', 'hey', 'hii', 'heyy']):
        return (
            "Ohooo entry maar di tumne 😌✨\n"
            "Itni cute 'hi' bhejne se pehle warning dena chahiye tha!\n"
            "Naam batao zara… ya main guess karun future wali wife ka? 😏"
        )

    if 'sneha' in processed:
        return (
            "SNEHAAA?? 😳🔥\n"
            "Dil ko shock lag gaya abhi toh!\n"
            "Tum online aati ho ya meri heartbeat test karne aati ho? 😏\n"
            "Sach bataun… tumhari smile pe already EMI chal rahi hai mere dil pe ❤️"
        )

    if 'sweata' in processed or 'sweta' in processed:
        return (
            "Areyyy Sweataaa 😂✨\n"
            "Drama queen mode ON hai ya normal human version me aayi ho aaj? 😌"
        )

    if 'no' in processed:
        return (
            "Itna straight 'no'? 😭\n"
            "Thoda emotional background music toh chalne do!\n"
            "Chalo theek hai… par reason toh do, main improvement plan banaunga 💪😌"
        )

    if 'how are you' in processed:
        return (
            "Main theek tha… phir tumhara message aaya 😌\n"
            "Ab thoda smile zyada aa raha hai.\n"
            "Tum batao, dil theek hai ya kisi ne already chura liya? 😏"
        )

    return (
        "System hang ho gaya 🫠\n"
        "Tum thoda clearly type karo na… ya phir bas dil ki baat seedha bol do 😌"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'user ({update.message.chat.id}) in {message_type}: "{text}')
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            next_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(next_text)
        else:
            return
        
    else:
        response: str = handle_response(text)
        
    print('Bot :', response)
    await update.message.reply_text(response)
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')
    

if __name__ == '__main__':
    print('Starting jarvis .....')
    
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('joke', jokes_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    app.add_error_handler(error)
    
    print('Polling .....')
    app.run_polling(poll_interval=2)
    