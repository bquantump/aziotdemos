#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) Microsoft Corporation.
# Licensed under the GNU General Public License v3.0 or later.
# See License.txt in the project root for license information.
#

import json
import os
import time
from azure.eventhub import EventHubProducerClient, EventData

CON_STRING = os.environ['EV_CON_STRING']

print(CON_STRING)
eventhub_producer = EventHubProducerClient.from_connection_string(
            conn_str=CON_STRING, eventhub_name='testiot')
mock = {'test': 'this is a test', 'again': 666}
jmsg = json.dumps(mock)
for _ in range(10000):
    print('sending...')
    event_batch = eventhub_producer.create_batch()
    event_batch.add(EventData(jmsg))
    eventhub_producer.send_batch(event_batch)
    time.sleep(2)
