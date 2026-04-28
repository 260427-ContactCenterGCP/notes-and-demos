# Google Cloud Platform (GCP)

## What is Cloud Computing?

Cloud computing is the on-demand delivery of computing services such as virtual machines, storage, databases, networking, and software over the internet.

Instead of purchasing and maintaining physical infrastructure, organizations can consume cloud resources as needed and pay only for what they use.

Google Cloud Platform (GCP) provides these services through Google’s global infrastructure, allowing businesses to build, deploy, and scale applications without managing physical hardware.

### Key Characteristics of Cloud Computing

- On-demand self-service
- Broad network access
- Resource pooling
- Rapid elasticity
- Measured service
- High availability
- Security and access control
- Cost efficiency

## Cloud Service Models

Cloud services are typically delivered in three primary models:

- **Infrastructure as a Service (IaaS)** – Virtualized compute, storage, and networking resources
- **Platform as a Service (PaaS)** – Managed platforms for building and deploying applications
- **Software as a Service (SaaS)** – Fully managed software delivered over the internet

Google Cloud offers services across all three models, depending on how much infrastructure management the user wants to retain.

<img src = "https://cms.webcreatify.com/gallery/1273-cloud-computing-2.png">

#### Pizzas As A Service

<img src = "https://miro.medium.com/max/1400/1*JacqOl2kjyTYzv31v0xITw.png">

---

# Global Infrastructure

## Regions and Zones

Google Cloud infrastructure is organized into **regions** and **zones**.

### Regions

A region is a specific geographic area where Google Cloud hosts infrastructure and services.

Regions allow organizations to deploy workloads closer to users for:

- Lower latency
- Better performance
- Regional compliance requirements

### Zones

A zone is an isolated deployment area within a region.

Each region contains multiple zones, and each zone is designed to operate independently from failures in other zones in the same region.

This design improves:

- Fault tolerance
- High availability
- Disaster recovery planning

Applications can be distributed across multiple zones to reduce the impact of infrastructure failure.

- [Regions and Zones](https://cloud.google.com/compute/docs/regions-zones)
- [View Available Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones)


---

# Compute Engine

## What is Compute Engine?

Google Compute Engine is Google Cloud’s Infrastructure as a Service (IaaS) compute platform.

It allows users to create and run virtual machines on Google’s global infrastructure.

These virtual machines can run:

- Web servers
- APIs
- Enterprise applications
- Background services
- Custom workloads

Compute Engine provides direct control over:

- Operating system
- CPU and memory configuration
- Storage
- Networking
- Security settings

This makes Compute Engine ideal when full control over the server environment is required.

## Compute Engine Virtual Machines

A Compute Engine Virtual Machine (VM) is a software-defined server running in Google Cloud.

Each VM includes:

- Virtual CPUs (vCPUs)
- Memory (RAM)
- Boot disk
- Network interfaces
- Operating system

These VMs behave like traditional servers, but are provisioned and managed in the cloud.

## Machine Types

Compute Engine offers predefined machine families optimized for different workloads.

Examples include:

- **E2** – Cost-optimized general-purpose workloads
- **N2** – Balanced performance and flexibility
- **C3** – Compute-optimized workloads
- **M3** – Memory-intensive enterprise workloads

Compute Engine also supports **custom machine types**, allowing users to define CPU and memory combinations tailored to their workload.

## Virtual Machine Images

VM instances are created from images.

An image is a bootable template used to create virtual machines and includes:

- Operating system
- Boot disk contents
- Preconfigured software
- System settings

Google Cloud provides:

- Public images maintained by Google
- Custom images created by users
- Machine images for full VM capture and reuse

Images help standardize and accelerate VM provisioning.

- [Compute Engine Overview](https://docs.cloud.google.com/compute/docs/overview)


---

# Block Storage

## Persistent Disk

Persistent Disk is Google Cloud’s durable block storage service for virtual machines.

It provides high-performance storage volumes that can be attached to Compute Engine instances.

Persistent Disk is commonly used for:

- Boot volumes
- Application storage
- Database storage

### Key Features

- Durable and network-attached
- Automatically encrypted at rest
- Can persist beyond the life of a VM
- Can be resized dynamically
- Available as zonal or regional storage

Because Persistent Disk is decoupled from the VM lifecycle, storage can remain intact even if the instance is stopped, deleted, or replaced.

- [Block Storage Overview](https://cloud.google.com/products/block-storage?hl=en)
- [Choosing a Disk Type](https://docs.cloud.google.com/compute/docs/disks)

---

# Managed Instance Groups (MIGs)

## What are Managed Instance Groups?

A Managed Instance Group (MIG) is a collection of virtual machines managed as a single logical service.

Each VM in the group is created from the same **instance template**, ensuring consistency across all instances.

Managed Instance Groups are commonly used for:

- Scalable web applications
- Stateless services
- Load-balanced applications
- Highly available compute tiers

## Key Capabilities

### Autoscaling

MIGs can automatically increase or decrease the number of VM instances based on demand.

Scaling policies can respond to:

- CPU utilization
- Load balancing traffic
- Monitoring metrics
- Scheduled demand

### Autohealing

MIGs continuously monitor instance health and automatically recreate failed VMs.

This improves service resilience without manual intervention.

### Load Balancing Integration

MIGs integrate directly with Google Cloud Load Balancing, making them a common foundation for scalable application architectures.

### Regional and Zonal MIGs

- **Zonal MIGs** run instances in a single zone
- **Regional MIGs** distribute instances across multiple zones for higher availability

- [Managed Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups)

---

# Firewall Rules

## GCP Firewall Rules

Google Cloud Firewall Rules control traffic flowing into and out of resources within a Virtual Private Cloud (VPC).

Unlike host-level firewall controls, GCP firewall rules are defined at the **VPC network level** and apply to resources within that network.

This makes firewalling in GCP centralized and network-aware.

## Firewall Rule Behavior

Firewall rules define:

- Allowed or denied traffic
- Source and destination ranges
- Protocols and ports
- Target instances

Rules can target resources using:

- Network tags
- Service accounts

This makes firewall policy flexible and scalable across environments.

## Key Characteristics

- Stateful traffic filtering
- Applied at the VPC level
- Centralized network policy enforcement
- Priority-based rule evaluation

Firewall rules are a foundational part of securing GCP workloads.

- [VPC Firewall Rules](https://docs.cloud.google.com/firewall/docs/firewalls)
---

# Cloud Storage

## What is Cloud Storage?

Google Cloud Storage is Google Cloud’s object storage service.

It is used to store and retrieve unstructured data such as:

- Files
- Images
- Videos
- Logs
- Backups
- Archived data

Cloud Storage is designed for durability, scalability, and global accessibility.

## Buckets and Objects

Cloud Storage stores data as **objects** inside **buckets**.

- A **bucket** is a top-level container for storing objects
- An **object** is the stored file and its associated metadata

Each object includes:

- Object name
- Data
- Metadata
- Generation number for versioning

## Storage Classes

Cloud Storage provides multiple storage classes optimized for different access patterns:

- **Standard** – Frequently accessed data
- **Nearline** – Infrequently accessed data
- **Coldline** – Rarely accessed data
- **Archive** – Long-term archival storage

This allows organizations to optimize cost based on retrieval frequency.

## Location Types

Cloud Storage buckets can be deployed in:

- **Regional** locations
- **Dual-region** locations
- **Multi-region** locations

This provides flexibility for performance, resilience, and compliance requirements.

- [Cloud Storage Overview](https://docs.cloud.google.com/storage/docs/introduction)

---

# Cloud SQL

## What is Cloud SQL?

Cloud SQL is Google Cloud’s fully managed relational database service.

It is designed for applications that need structured relational data without requiring teams to manage database infrastructure manually.

Cloud SQL supports:

- MySQL
- PostgreSQL
- SQL Server

## Why Use Cloud SQL?

Cloud SQL simplifies database operations by automating:

- Provisioning
- Backups
- Patching
- Replication
- Failover
- Maintenance

This reduces operational overhead and allows teams to focus on application development.

## Security and Connectivity

Cloud SQL integrates with Google Cloud security and networking features, including:

- IAM
- Private IP connectivity
- VPC access controls
- Encryption at rest and in transit

Applications commonly connect using:

- Native database clients
- Cloud SQL connectors
- Cloud SQL Auth Proxy

## Common Use Cases

Cloud SQL is commonly used for:

- Web applications
- Backend APIs
- Business systems
- Transactional applications
- Managed relational workloads

- [Cloud SQL Overview](https://docs.cloud.google.com/sql/docs/introduction)

---

# Cloud Deployment Manager

Read the following information regarding leveraging the Cloud Deployment Manager through the Cloud Shell to deploy infrastructure as code.

[Cloud Deployment Manager](https://www.geeksforgeeks.org/google-cloud-deployment-manager/)