import argparse
import os
import time

import googleapiclient.discovery
from six.moves import input

compute = googleapiclient.discovery.build('compute', 'v1')

# Var
ZONE = "europe-west6-a"
PROJECT = "cloudsys-lab1-364500"


# List instances
def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None


x = list_instances(compute, PROJECT, ZONE)
print(x)


# Instance config of server
server_config = {
    "canIpForward": False,
    "confidentialInstanceConfig": {
        "enableConfidentialCompute": False
    },
    "deletionProtection": False,
    "description": "",
    "disks": [
        {
            "autoDelete": True,
            "boot": True,
            "deviceName": "cloudsys-lab1-server",
            "initializeParams": {
                "diskSizeGb": "10",
                "diskType": "projects/cloudsys-lab1-364500/zones/us-central1-a/diskTypes/pd-balanced",
                "labels": {}
            },
            "mode": "READ_WRITE",
            "type": "PERSISTENT"
        }
    ],
    "displayDevice": {
        "enableDisplay": False
    },
    "guestAccelerators": [],
    "keyRevocationActionType": "NONE",
    "labels": {},
    "machineType": "projects/cloudsys-lab1-364500/zones/europe-west6-a/machineTypes/e2-small",
    "metadata": {
        "items": [
            {
                "key": "startup-script",
                "value": "apt -y update\napt -y install git\napt -y install python3-pip\npip3 install \"fastapi[all]\"\napt -y install uvicorn \ncd /home/ubuntu\ngit clone https://github.com/Danielcourvoisier/cloudsys-lab1-server.git\nexport BUCKET_URL=https://storage.googleapis.com/cloudsys-lab1-bucket/test.json\nexport APP_PORT=8080\ncd /home/ubuntu/cloudsys-lab1-server/\nuvicorn main:app --host 0.0.0.0 --port $APP_PORT"
            }
        ]
    },
    "minCpuPlatform": "Automatic",
    "name": "cloudsys-lab1-server",
    "networkInterfaces": [
        {
            "accessConfigs": [
                {
                    "name": "External NAT",
                    "natIP": "34.65.95.230",
                    "networkTier": "PREMIUM"
                }
            ],
            "stackType": "IPV4_ONLY",
            "subnetwork": "projects/cloudsys-lab1-364500/regions/europe-west6/subnetworks/default"
        }
    ],
    "reservationAffinity": {
        "consumeReservationType": "ANY_RESERVATION"
    },
    "scheduling": {
        "automaticRestart": True,
        "onHostMaintenance": "MIGRATE",
        "preemptible": False,
        "provisioningModel": "STANDARD"
    },
    "serviceAccounts": [
        {
            "email": "865720766122-compute@developer.gserviceaccount.com",
            "scopes": [
                "https://www.googleapis.com/auth/devstorage.read_only",
                "https://www.googleapis.com/auth/logging.write",
                "https://www.googleapis.com/auth/monitoring.write",
                "https://www.googleapis.com/auth/servicecontrol",
                "https://www.googleapis.com/auth/service.management.readonly",
                "https://www.googleapis.com/auth/trace.append"
            ]
        }
    ],
    "shieldedInstanceConfig": {
        "enableIntegrityMonitoring": True,
        "enableSecureBoot": False,
        "enableVtpm": True
    },
    "sourceMachineImage": "projects/cloudsys-lab1-364500/global/machineImages/cloudsys-lab1-server-image",
    "tags": {
        "items": [
            "http-server",
            "https-server"
        ]
    },
    "zone": "projects/cloudsys-lab1-364500/zones/europe-west6-a"
}

# Instance config of server
client_config = {
  "canIpForward": False,
  "confidentialInstanceConfig": {
    "enableConfidentialCompute": False
  },
  "deletionProtection": False,
  "description": "",
  "disks": [
    {
      "autoDelete": True,
      "boot": True,
      "deviceName": "cloudsys-lab1-client",
      "initializeParams": {
        "diskSizeGb": "10",
        "diskType": "projects/cloudsys-lab1-364500/zones/us-central1-a/diskTypes/pd-balanced",
        "labels": {}
      },
      "mode": "READ_WRITE",
      "type": "PERSISTENT"
    }
  ],
  "displayDevice": {
    "enableDisplay": False
  },
  "guestAccelerators": [],
  "keyRevocationActionType": "NONE",
  "labels": {},
  "machineType": "projects/cloudsys-lab1-364500/zones/europe-west6-a/machineTypes/e2-small",
  "metadata": {
    "items": [
      {
        "key": "startup-script",
        "value": "apt -y update\napt -y install git\napt -y install python3-pip\npip3 install \"fastapi[all]\"\napt -y install uvicorn\ncd /home/ubuntu\ngit clone https://github.com/Danielcourvoisier/cloudsys-lab1-client.git\nexport SERVER_IP=34.65.95.230\nexport SERVER_PORT=8080\nexport APP_PORT=8080\ncd /home/ubuntu/cloudsys-lab1-client/\nuvicorn main:app --host 0.0.0.0 --port $APP_PORT"
      }
    ]
  },
  "minCpuPlatform": "Automatic",
  "name": "cloudsys-lab1-client",
  "networkInterfaces": [
    {
      "accessConfigs": [
        {
          "name": "External NAT",
          "natIP": "34.65.117.125",
          "networkTier": "PREMIUM"
        }
      ],
      "stackType": "IPV4_ONLY",
      "subnetwork": "projects/cloudsys-lab1-364500/regions/europe-west6/subnetworks/default"
    }
  ],
  "reservationAffinity": {
    "consumeReservationType": "ANY_RESERVATION"
  },
  "scheduling": {
    "automaticRestart": True,
    "onHostMaintenance": "MIGRATE",
    "preemptible": False,
    "provisioningModel": "STANDARD"
  },
  "serviceAccounts": [
    {
      "email": "865720766122-compute@developer.gserviceaccount.com",
      "scopes": [
        "https://www.googleapis.com/auth/devstorage.read_only",
        "https://www.googleapis.com/auth/logging.write",
        "https://www.googleapis.com/auth/monitoring.write",
        "https://www.googleapis.com/auth/servicecontrol",
        "https://www.googleapis.com/auth/service.management.readonly",
        "https://www.googleapis.com/auth/trace.append"
      ]
    }
  ],
  "shieldedInstanceConfig": {
    "enableIntegrityMonitoring": True,
    "enableSecureBoot": False,
    "enableVtpm": True
  },
  "sourceMachineImage": "projects/cloudsys-lab1-364500/global/machineImages/cloudsys-lab1-client-image",
  "tags": {
    "items": [
      "http-server",
      "https-server"
    ]
  },
  "zone": "projects/cloudsys-lab1-364500/zones/europe-west6-a"
}

# Create server instance
server = compute.instances().insert(project=PROJECT, zone=ZONE, body=server_config).execute()

# Create server instance
client = compute.instances().insert(project=PROJECT, zone=ZONE, body=client_config).execute()

input("Press Enter to delete instances:")

compute.instances().delete(project=PROJECT,
                           zone=ZONE,
                           instance="cloudsys-lab1-server").execute()

compute.instances().delete(project=PROJECT,
                           zone=ZONE,
                           instance="cloudsys-lab1-client").execute()
