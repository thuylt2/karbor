#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

OPTIONS_SCHEMA = {
    "title": "Share Protection Options",
    "type": "object",
    "properties": {
        "snapshot_name": {
            "type": "string",
            "title": "Snapshot Name",
            "description": "The name of the snapshot.",
            "default": None
        },
        "description": {
            "type": "string",
            "title": "Description",
            "description": "The description of the volume."
        },
        "force": {
            "type": "boolean",
            "title": "Force",
            "description": "Whether to backup, even if the volume "
                           "is attached",
            "default": False
        }
    },
    "required": ["snapshot_name", "force"]
}

RESTORE_SCHEMA = {
    "title": "Share Protection Restore",
    "type": "object",
    "properties": {
        "restore_name": {
            "type": "string",
            "title": "Restore Share Name",
            "description": "The name of the restore share",
            "default": None
        },
    },
    "required": ["restore_name"]
}

SAVED_INFO_SCHEMA = {
    "title": "Share Protection Saved Info",
    "type": "object",
    "properties": {},
    "required": []
}
