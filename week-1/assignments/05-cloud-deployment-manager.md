\# Cloud Deployment Manager Assignment



\## Overview



In this assignment, you will use \*\*Google Cloud Deployment Manager\*\* to define and deploy infrastructure as code using a YAML configuration file. This exercise will help you understand how to automate resource provisioning in GCP.



\## Instructions



\### Step 1: Enable Deployment Manager API



\* Log in to the \[Google Cloud Console](https://console.cloud.google.com).

\* Make sure you’ve selected or created a project.

\* In the left-hand menu, go to \*\*APIs \& Services > Library\*\*.

\* Search for \*\*Deployment Manager V2 API\*\* and enable it.



\### Step 2: Open Cloud Shell and Create a Configuration File



\* Open \*\*Cloud Shell\*\* from the top-right corner of the console.

\* Create a directory to hold your configuration files:



&#x20; ```bash

&#x20; mkdir gcp-deployment \&\& cd gcp-deployment

&#x20; ```

\* Create a file named `vm-config.yaml` with the following content:



&#x20; ```yaml

&#x20; resources:

&#x20; - name: demo-vm

&#x20;   type: compute.v1.instance

&#x20;   properties:

&#x20;     zone: us-central1-a

&#x20;     machineType: zones/us-central1-a/machineTypes/e2-micro

&#x20;     disks:

&#x20;     - deviceName: boot

&#x20;       type: PERSISTENT

&#x20;       boot: true

&#x20;       autoDelete: true

&#x20;       initializeParams:

&#x20;         sourceImage: projects/debian-cloud/global/images/family/debian-11

&#x20;     networkInterfaces:

&#x20;     - network: global/networks/default

&#x20;       accessConfigs:

&#x20;       - name: External NAT

&#x20;         type: ONE\_TO\_ONE\_NAT

&#x20; ```



\### Step 3: Create the Deployment



\* Run the following command to deploy the configuration:



&#x20; ```bash

&#x20; gcloud deployment-manager deployments create demo-deployment --config vm-config.yaml

&#x20; ```

\* Wait for the deployment to finish. Then go to \*\*Compute Engine > VM instances\*\* to confirm the instance was created.



\### Step 4: Validate and Clean Up



\* Connect to the VM using SSH from the \*\*Compute Engine\*\* section.

\* Run:



&#x20; ```bash

&#x20; echo "Deployment successful!"

&#x20; ```

\* To clean up (optional but recommended after the assignment):



&#x20; ```bash

&#x20; gcloud deployment-manager deployments delete demo-deployment

&#x20; ```



\## Requirements



\* Deployment Manager must be used to create a VM named `demo-vm`.

\* A valid YAML file (`vm-config.yaml`) must define the deployment.

\* VM should be visible in the Compute Engine console.

