# Cloud Deployment Manager Assignment



## Overview



In this assignment, you will use **Google Cloud Deployment Manager** to define and deploy infrastructure as code using a YAML configuration file. This exercise will help you understand how to automate resource provisioning in GCP.



## Instructions



### Step 1: Enable Deployment Manager API



* Log in to the [Google Cloud Console](https://console.cloud.google.com).

* Make sure you’ve selected or created a project.

* In the left-hand menu, go to **APIs & Services > Library**.

* Search for **Deployment Manager V2 API** and enable it.



### Step 2: Open Cloud Shell and Create a Configuration File



* Open **Cloud Shell** from the top-right corner of the console.

* Create a directory to hold your configuration files:



    ```bash

    mkdir gcp-deployment && cd gcp-deployment

    ```

* Create a file named `vm-config.yaml` with the following content:



    ```yaml
  resources:
  - name: demo-vm
    type: compute.v1.instance
    properties:
      zone: us-central1-a
      machineType: zones/us-central1-a/machineTypes/e2-micro
      disks:
      - deviceName: boot
        type: PERSISTENT
        boot: true
        autoDelete: true
        initializeParams:
          sourceImage: projects/debian-cloud/global/images/family/debian-11
      networkInterfaces:
      - network: global/networks/default
        accessConfigs:
        - name: External NAT
          type: ONE_TO_ONE_NAT
  ```

### Step 3: Create the Deployment

* Run the following command to deploy the configuration:

    ```bash

    gcloud deployment-manager deployments create demo-deployment --config vm-config.yaml

    ```

* Wait for the deployment to finish. Then go to **Compute Engine > VM instances** to confirm the instance was created.

### Step 4: Validate and Clean Up

* Connect to the VM using SSH from the **Compute Engine** section.

* Run:

    ```bash

    echo "Deployment successful!"

    ```

* To clean up (optional but recommended after the assignment):

    ```bash

    gcloud deployment-manager deployments delete demo-deployment

    ```

## Requirements

* Deployment Manager must be used to create a VM named `demo-vm`.

* A valid YAML file (`vm-config.yaml`) must define the deployment.

* VM should be visible in the Compute Engine console.

