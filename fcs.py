import logging

from telegram.ext import (
    Updater, CommandHandler, MessageHandler, Filters)

from telegram import InputMediaPhoto


log = logging.getLogger(__name__)


class FaceStyleBot:
    def __init__(self, args):
        self.token = args.token
        self.debug_id = args.debug_user

    def debug(self, text):
        """Send debug TEXT to debug_id user.
        Also log with DEBUG level."""
        log.debug(text)

        if self.debug_id:
            self.bot.send_message(chat_id=self.debug_id, text=text)

    def on_start(self, bot, update):
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Send me a photo of facial")

    def on_photo(self, bot, update):
        msg = update.message

        self.debug('Incoming %d photos from: @%s' % (
            len(msg.photo), msg.chat['username']))

        with open('/home/lg/Downloads/circle_face.jpeg', 'rb') as pfile:
            bot.send_photo(
                chat_id=msg.chat_id,
                photo=pfile)

    def on_error(self, bot, update, tg_err):
        if self.debug_id:
            bot.send_message(
                chat_id=self.debug_id,
                text='Error: %s' % tg_err)

    def run(self):
        updater = Updater(self.token)
        self.bot = updater.bot

        updater.dispatcher.add_handler(
            CommandHandler('start', self.on_start))
        updater.dispatcher.add_handler(
            MessageHandler(Filters.photo, self.on_photo))
        updater.dispatcher.add_error_handler(self.on_error)

        updater.start_polling()
        updater.idle()
