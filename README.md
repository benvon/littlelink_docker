# LittleLink (Docker version)

This project is a fork of [LittleLink](https://github.com/sethcottle/littlelink). I wanted to create a Docker version of this project that is not modify and kept to true original. And that is what I have done here with the exception of creating the docker files in this repo.

LittleLink is a lightweight DIY alternative to services like [Linktree](https://linktr.ee)
and [many.link](https://many.link/). LittleLink was built using [Skeleton](http://getskeleton.com/), a dead simple, responsive boilerplate—we just stripped out some additional code you wouldn't need and added in branded styles for popular services. 😊

To help you start with creating a container from this image, you can either use docker-compose or the docker command line. This container image is published on [DockerHub](https://hub.docker.com/r/davisdre/littlelink). 

### docker-compose (recommended)

```
version: "3"
services: 
  little-link:
    image: davisdre/littlelink:latest
    container_name: littlelink-server
    ports: 
      - 80:80
```

### docker commandline

```
docker run -d \
  --name=littlelink-server \
  -p 80:80
  davisdre/littlelink:latest
```

## Support
If you would like to support this docker build, please feel free to buy me a coffee!

<a href="https://www.buymeacoffee.com/davisdredotcom"> <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210"></a>

## Updates
- **Sep 1, 2021** 
  - Initial pull.
- **Oct 1, 2021** 
  - Pulled latest. 
  - Updated Docker with latest content.
- **Oct 31, 2021** 
  - Pulled latest from sethcottle/littelink. 
  - Updated Docker image.
- **Dec 13, 2021** 
  - Pulled latest. 
  - Updated Docker containers with latest content and security patches. 
- **Jan 28, 2022** 
  - Pulled latest. 
  - Updated Docker contrainers with latest content and security patches. 
- **Feb 17, 2022**
  - Pulled latest. 
  - Updated Docker contrainers with latest content and security patches.
- **Jun 01, 2022**
  - Merged latest from sethcottle/littelink.
  - Updated Dockerfile to reduce vulnearbilities.
  - Added .dockerigrone file to prevent copying of unecessary stuff into docker image. Kudos to [benvon](https://github.com/benvon) for the request.

# What is littlelink?

![LittleLink](https://cdn.cottle.cloud/littlelink/social-circle.png)

LittleLink is a lightweight DIY alternative to services like [Linktree](https://linktr.ee)
and [many.link](https://www.google.com). LittleLink was built using [Skeleton](http://getskeleton.com/), a dead simple, responsive boilerplate—we just stripped out some additional code you wouldn't need and added in branded styles for popular services. 😊

### 🤝 Community Extras

#### 🎨 Figma
Duplicate the [LittleLink Template on Figma Community](https://www.figma.com/community/file/846568099968305613) to help plan out and design your LittleLink page.

#### 🐋 Docker
[Techno Tim](https://github.com/timothystewart6) is building [LittleLink-Server](https://github.com/techno-tim/littlelink-server). Check out [his video](https://youtu.be/42SqfI_AjXU)!

[Drew](https://github.com/davisdre) is building a [super simple Docker implementation of LittleLink](https://github.com/davisdre/littlelink).

#### 🗃️ Misc
[Khashayar](https://github.com/khashayarzavosh) is building [LittleLink Admin](https://github.com/khashayarzavosh/admin-littlelink) which lets you host your own admin portal to manage LittleLink!

[Julian](https://github.com/JulianPrieber) is building [LittleLink Custom](https://github.com/JulianPrieber/littlelink-custom) which approaches the admin portal with an easy-to-use "plug-and-play" mentality!

---

### 💖 Supporters
You can support LittleLink by [buying me a beer](https://www.buymeacoffee.com/seth). You can also have your name or your company added to this section and the supporters page of the [LittleLink.io](https://littlelink.io) website.

#### 🏢 Business Supporters
[Add Your Company Name](https://www.buymeacoffee.com/seth/e/50574)

#### ✨ Individual Supporters
**[Drew Davis](https://connect.davisdre.me)**

**[Robotter112](https://robotter112.de/)**

[Add Your Name](https://www.buymeacoffee.com/seth/e/50573)

---

### 📊 Analytics

To help build a more privacy focused product, we recommend using [Fathom Analytics](https://usefathom.com/ref/EQVZMV)*. On May 03, 2022 we moved [LittleLink.io](https://littlelink.io) from Google Analytics to Fathom! We're also making our analytics dashboard [publicly available](https://app.usefathom.com/share/xbmnwxxl/littlelink.io#/?filters=%5B%5D&range=last_7_days&site=2251799827005303)** for everyone to view.

###### * This is a referral link. Using this link to sign up for Fathom is an easy way to help support LittleLink!

###### ** Analytics displayed in this dashboard start May 03, 2022. View this [Google Sheets file](https://docs.google.com/spreadsheets/d/1GL4SroAdH-OZphBVR5z-BoSukHIEVJfao25q_e9-Ii8/edit?usp=sharing) with the generic unique pageview data from Google Analytics.

