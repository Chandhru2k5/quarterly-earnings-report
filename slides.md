---
marp: true
theme: default
paginate: true
footer: '23f3001440@ds.study.iitm.ac.in'
style: |
  section {
    background-color: #ffffff;
    color: #222;
    font-family: Arial, sans-serif;
  }
  h1 {
    color: #005bbb;
  }
---

# Product Documentation

Modern technical documentation built using **Marp**  
**Contact:** 23f3001440@ds.study.iitm.ac.in

---

## Getting Started

Welcome to the official product documentation.  
This guide covers architecture, APIs, performance, and deployment.

---

## API Authentication

Use API key in request header:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.example.com/data
