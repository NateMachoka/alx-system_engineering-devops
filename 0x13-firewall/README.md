# UFW Firewall Configuration

## Project Overview

This project demonstrates how to configure the UFW (Uncomplicated Firewall) on an Ubuntu server to enhance its security. UFW is a frontend for managing iptables firewall rules, designed to be easy to use. In this project, we will set up UFW to block all incoming traffic except for the following TCP ports:
- 22 (SSH)
- 80 (HTTP)
- 443 (HTTPS)

## Requirements

- Ubuntu server
- sudo privileges

## Installation and Configuration Steps

### Step 1: Update Package List and Install UFW

First, update the package list to ensure you have the latest information about available packages. Then, install UFW.

```bash
sudo apt update
sudo apt install ufw -y
