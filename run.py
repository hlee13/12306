# -*- coding=utf-8 -*-
import sys

from init import login, select_ticket_info
from config import ticketConf as tc


def run():
    # login.main()
    if len(sys.argv) > 1:
      tc.config_file = sys.argv[1]
    select_ticket_info.select().main()


if __name__ == '__main__':
    run()
