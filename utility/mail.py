#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from DjFalcon.settings import EMAIL_HOST_USER
import threading

from_email = EMAIL_HOST_USER


class EmailThread(threading.Thread):

    def __init__(self, subject, text_content, html_content, sender_email, recipient_list, html):
        self.subject = subject
        self.text_content = text_content
        self.html_content = html_content
        self.sender_email = sender_email
        self.recipient_list = recipient_list
        self.html = html
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMultiAlternatives(self.subject, self.text_content, self.sender_email, self.recipient_list)
        if self.html:
            msg.attach_alternative(self.html_content, self.html)
            msg.send()


def send_mail(subject, content, html_content, sender_email, recipient_list, html=None, *args, **kwargs):
    EmailThread(subject, content, html_content, sender_email, recipient_list, html).start()


if __name__ == "__main__":
    sub = '标题a'
    to = ["844743779@qq.com"]
    content = 'This is an important message'
    html_content = '<p>这是一封<strong>重要的</strong>邮件.</p>'
    print("aaaaaaaaaaaaa")
    send_mail(sub, content, html_content, from_email, to, html="text/html")
