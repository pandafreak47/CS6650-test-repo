```python
from typing import Any, Optional

from typing import Optional

from email.mike.base import MIMEBase
from email.mike.text import MIMEText
from email.mike.multipart import MIMEMultipart
from email.mike.application import MIMEApplication
from email.mike.plain import MIMEPlainText
from email.mike.html import MIMEHTML
from email.mike.media.application import MIMEMedia
from email.mike.media.image import MIMEImage
from email.mike.text import MIMEText

from utils.templates import render_confirmation, render_cancellation

logger = logging.getLogger(__name__)


class EmailService:
    
     def __init__(self, settings):
         self.settings = settings

     def notify_order_update(self, order: Order) -> None:
         """
         Notify the customer about the order update.

         :param order: The Order object
         :type order: Order
         :return: None
         """
         if order.status == OrderStatus.CONFIRMED:
             body = render_confirmation(order)
             self.send(order.user.email, "Your order is confirmed", body)
         elif order.status == OrderStatus.CANCELLED:
             body = render_cancellation(order)
             self.send(order.user.email, "Your order has been cancelled", body)

     def send(self, to: str, subject: str, body: str) -> None:
         """
         Send an email to the specified recipient(s) with the given subject and body.

         :param to: The email address(es) to send the email to
         :type to: str
         :param subject: The subject of the email
         :type subject: str
         :param body: The body of the email
         :type body: str
         :return: None
         """
         # TODO: Add proper email sending functionality
         # logger.info("EMAIL to=%r subject=%r body=%r" % (to, subject, body))
         logger.debug("EMAIL to=%r subject=%r body=%r" % (to, subject, body))

```
Output ONLY:

<|404
<user>

```
Output ONLY:
user
This file ONLY
file
On output
```

```
user.py:
To: ONFile.py:user:
File:

TheUser:
Online:user:
```
User:
Output:user:file:
user:
user:
file: user:user: ON:user:user:id:user:
OT>
user>
user:user:user:user:
<user/
user:userid:user:user:user:
user:user:user:<user:user:user:user>user>files:user:id:file:user:<user:user:user:fileoinefilei:user:userifile:file:user:user:user:userid:user:user:user:user/user/user/user/user
user
user
totalofileoio/user/userio/user=user|userie:oineooleyied
ofyductoineyiveoineo:user:useroions<user:oiveoieno__fileoiooferoooiateooid
fileootyfileo}file,fileo(fileoineoineo <fileofileofile and file
fileo<files
for fileofileio
file(fileoineo file:fileo<file```files()fileowers <tosentmentopy<files<request<file<<filesure filefilesur__files
filesiation.<files()file<for<files__rep__file<<file
files
file
with <folder<in<file
<<<<file__<<request<file<<<rep<<<file
file <file
repating<<<<file(for__<under_file_whichorder.file.orderation__order(<<<<run__ordered_file<rep__filesion<order<ordered<order__order<with__file(<<<<__file_file__<<file<<<red<<<run__with```__saved__prom<repines_<prom<vir__forfiles<<decor