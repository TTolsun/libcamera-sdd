# Glossary

English translation · human review pending. Review states below refer to the Korean source.

**Collects the meanings of abbreviations and domain terms that appear in the document.**

Select an underlined term in the body text to see its meaning in place. You can also search for the term by name in document search.

Quick links: [0–9](#d1-term-3a) · [A](#d1-term-af) · [B](#d1-term-bayer) · [C](#d1-term-ccm) · [D](#d1-term-debug) · [E](#d1-term-ebusy) · [F](#d1-term-fbo) · [G](#d1-term-gb) · [H](#d1-term-hal) · [I](#d1-term-ipa) · [L](#d1-term-log) · [M](#d1-term-mali-c55) · [N](#d1-term-nv12) · [O](#d1-term-omm) · [P](#d1-term-pending) · [Q](#d1-term-qbuf) · [R](#d1-term-raw) · [S](#d1-term-streamoff) · [T](#d1-term-tid) · [U](#d1-term-udmabuf) · [V](#d1-term-v4l2) · [W](#d1-term-wsl) · [ㄷ](#d1-term-%EB%94%94%EB%B2%A0%EC%9D%B4%EC%96%B4) · [ㅁ](#d1-term-%EB%A9%94%ED%83%80%EB%8D%B0%EC%9D%B4%ED%84%B0) · [ㅂ](#d1-term-%EB%B8%94%EB%9E%99-%EB%A0%88%EB%B2%A8) · [ㅅ](#d1-term-%EC%85%B0%EC%9D%B4%EB%8D%94) · [ㅇ](#d1-term-%EC%99%9C%EA%B3%A1-%EB%B3%B4%EC%A0%95) · [ㅋ](#d1-term-%EC%BB%A8%ED%8A%B8%EB%A1%A4-%EC%A0%95%EB%B3%B4-%EB%A7%B5) · [ㅌ](#d1-term-%ED%8A%9C%EB%8B%9D-%ED%8C%8C%EC%9D%BC) · [ㅍ](#d1-term-%ED%94%84%EB%A0%88%EC%9E%84-%EB%B2%84%ED%8D%BC) · [ㅎ](#d1-term-%ED%99%9C%EC%84%B1-%EC%8A%A4%ED%8A%B8%EB%A6%BC)

- <a id="d1-term-3a"></a>**3A**: A collective term for auto exposure (AE/AGC), auto white balance (AWB), and auto focus (AF). These are representative algorithms that the IPA computes.
- <a id="d1-term-af"></a>**AF** (Auto Focus): An algorithm that moves the lens position to bring the image into focus.
- **AGC** (Automatic Gain Control): An automatic exposure algorithm that sets the exposure time and sensor gain to match scene brightness.
- **ASSERT**: libcamera's debug-check macro. In debug builds, if the condition is false, it logs a fatal message and aborts execution.
- **AWB** (Auto White Balance): An algorithm that estimates the color temperature of the illumination and sets per-channel R, G, and B gains so that white appears white.
- <a id="d1-term-bayer"></a>**bayer**: A color filter array in which each pixel of the sensor records only one color among R, G, and B. Raw data in this format must go through demosaicing before each pixel has RGB values.
- <a id="d1-term-ccm"></a>**CCM**: Means the IPU3 color correction matrix algorithm.
- <a id="d1-term-debug"></a>**DEBUG**: The name of the most verbose diagnostic level among log severity levels. Setting the log level environment variable to \`DEBUG\` yields detailed logs.
- **DMA** (Direct Memory Access): DMA (Direct Memory Access) is a term for a method in which an I/O device reads from or writes to system memory directly.
- **DQBUF**: DQBUF is an ioctl command that requests the next available buffer to be dequeued from a V4L2 device.
- **DRM** (Direct Rendering Manager): A kernel subsystem that manages Linux graphics devices. DRM pixel formats identify the channel layout within a buffer.
- **DW100**: A separate hardware device that corrects distortion by remapping the image according to a coordinate table. It is included in the NXP i.MX8MP and similar parts.
- <a id="d1-term-ebusy"></a>**EBUSY**: If FrameBufferAllocator::allocate() is called again for a stream that already has buffers allocated, it returns -EBUSY.
- **EEXIST**: Returns the -EEXIST error when a buffer still has an unreleased fence or a buffer is already registered on the same stream.
- **EGL**: An interface that connects the graphics API with the display, image, and buffer of the operating environment. This document covers the boundary where shared buffers are imported as graphics images.
- **errno**: The standard error number that Linux functions use to report the cause of a failure. libcamera functions return this value as a negative number. For example, -ENODEV means no device, -EACCES means access denied, -EINVAL means invalid argument, -ENOMEM means out of memory, and -EXDEV means a resource that belongs to another object.
- **ETIMEDOUT**: An error code indicating that the IPC response wait timer has expired. The timer setting value in this document is 2000ms.
- <a id="d1-term-fbo"></a>**FBO**: Refers to a frame buffer object to which a texture is to be attached.
- **fence**: A synchronization signal that indicates when a buffer may be used. If a valid fence is attached to a request, the request waits for this signal in the preparation stage. It is different from the request completion signal.
- **FPS**: The number of frames per second.
- <a id="d1-term-gb"></a>**GB**: Means the green B shading coefficient in the lens shading correction table.
- **GCC** (GNU Compiler Collection): A collection of GNU compilers that includes front ends for C, C++, and other languages.
- **GDB** (GNU Project Debugger): A GNU debugger that stops a program under specified conditions and lets you examine its execution state after it stops.
- **GL**: A prefix used in identifiers of OpenGL-family graphics APIs. In this document, GL formats indicate the channel composition of a texture.
- **GNU** (GNU's Not Unix): GNU is an operating system composed of free software. The name is a recursive acronym meaning GNU's Not Unix.
- **GR**: Means the green R shading coefficient in the lens shading correction table.
- <a id="d1-term-hal"></a>**HAL** (Hardware Abstraction Layer): A layer that lets the operating system handle hardware that differs by manufacturer through the same interface. The final deployment target of this project is the in-house Android Camera HAL.
- <a id="d1-term-ipa"></a>**IPA** (Image Processing Algorithms): A separate module (.so) that contains image quality algorithms. It reads the statistics sent by the ISP and calculates the ISP settings to use for the next frame. It is separated from the libcamera core so that manufacturers can provide it without publishing its source.
- **IPC** (Inter-Process Communication): A method by which separate processes exchange messages. Because an unsigned IPA module runs in a separate process, libcamera calls it through IPC.
- **IPU** (Image Processing Unit): The name of Intel's family of image processing units. Generation numbers are attached to the name, as in IPU3 and IPU6.
- **IPU3** (Intel Image Processing Unit 3): A camera ISP included in some Intel laptop processors. libcamera has a Pipeline Handler and an IPA for this device.
- **IPU6**: One generation of the Intel Image Processing Unit (IPU). The official documentation lists it as a supported target of the simple pipeline handler instead of a dedicated handler.
- **ISP** (Image Signal Processor): A processing unit that converts raw (Bayer) data output by the sensor into an image that can be displayed on screen. It performs operations such as black level correction, lens shading correction, white balance, and debayering.
- <a id="d1-term-log"></a>**LOG**: Uses the category and severity level specified by the caller.
- **LSC** (Lens Shading Correction): Processing that corrects lens shading, the phenomenon in which the edges of an image are darker than the center or colors are distorted due to lens characteristics. It is applied by multiplying by a correction table that divides the image into a grid.
- **LUT** (Look-Up Table): A method that precomputes calculation results into a table and retrieves them directly by input value. The LSC correction table falls into this category.
- <a id="d1-term-mali-c55"></a>**mali-c55**: Arm Mali-C55 camera ISP. libcamera has a Pipeline Handler and an IPA for this device.
- **mojom**: A file format that defines the functions and data types of the IPA interface. Proxy code is generated from this definition at build time.
- <a id="d1-term-nv12"></a>**NV12** (NV12): A 4:2:0 format that uses 8 bits per component. The first plane is luminance (Y). The second plane contains interleaved chroma data, in which Cb and Cr values are stored alternately, one each. The whole layout is placed in linearly contiguous memory.
- <a id="d1-term-omm"></a>**OMM**: An external documentation tool referenced by this site's reading-layout, figure zoom, and search rules. Only the rules were applied; the tool's runner was not used.
- <a id="d1-term-pending"></a>**Pending**: The request state in which the request has not yet changed to completed or canceled. It does not mean device processing has started, and if a preceding request is in this state, the return of a following request may also have to wait.
- **Pipeline Handler**: A libcamera component that finds the media device of a specific hardware platform (IPU3, RKISP1, etc.), creates cameras, passes requests to the device, and returns their completion. There is one per platform.
- **PR** (Pull Request): A request proposing that code changes be merged into the project.
- <a id="d1-term-qbuf"></a>**QBUF**: An ioctl that requests the addition of a buffer to the V4L2 device's queue.
- <a id="d1-term-raw"></a>**RAW**: RAW is a pixel color-encoding classification and is distinguished from StreamRole::Raw, a separate stream role for capturing raw sensor frames.
- **RK3399**: Rockchip's system-on-chip (SoC). The official documentation lists it as a supported target of the rkisp1 pipeline handler.
- **RKISP1** (Rockchip Image Signal Processor 1): A camera ISP included in Rockchip SoCs, the NXP i.MX8MP, and others. libcamera has a Pipeline Handler and an IPA for this device.
- **ROI** (Return on Investment): ROI is a concept that compares returns with investment costs, and it is not measured in this example from the public libcamera documentation.
- <a id="d1-term-streamoff"></a>**STREAMOFF**: An ioctl that requests streaming to be stopped for the specified buffer type on a V4L2 device.
- <a id="d1-term-tid"></a>**TID** (Linux thread ID): A TID is the Linux thread ID returned by the gettid system call.
- <a id="d1-term-udmabuf"></a>**UDMABUF** (userspace dmabuf misc driver): A Linux kernel driver name for a driver that converts a userspace memfd region into a dma-buf.
- **UQ**: An unsigned fixed-point format. UQ\<m, n\> represents a value with m bits for the integer part and n bits for the fractional part.
- **UVC** (USB Video Class): The standard that USB webcams follow. libcamera handles this device with the uvcvideo Pipeline Handler.
- <a id="d1-term-v4l2"></a>**V4L2** (Video4Linux2): The API through which the Linux kernel handles cameras and video devices. libcamera uses this API to control the sensor and ISP devices.
- **VM** (Virtual Machine): A virtual machine is a computer implemented in software by virtualizing the resources of a physical computer, and it runs its own operating system and applications. It is not limited to cloud servers and can also be created on a personal physical computer.
- <a id="d1-term-wsl"></a>**WSL** (Windows Subsystem for Linux): A Windows feature that lets you run a Linux environment on a Windows computer.
- **WSL2** (Windows Subsystem for Linux 2): An environment for running Linux on Windows. This site is built from the results of building and extracting libcamera on WSL2.
- <a id="d1-term-디베이어"></a>**Debayer**: A process that interpolates the missing colors of each pixel from neighboring pixels in bayer raw data to create an RGB image. Also called demosaicing.
- <a id="d1-term-메타데이터"></a>**Metadata**: Capture information checked alongside the image pixels. The metadata of a Request is provided as a ControlList, and the FrameMetadata of a FrameBuffer holds capture status, timestamp, bytes used, and so on. Whether the other fields of FrameMetadata are valid depends on the capture status.
- <a id="d1-term-블랙-레벨"></a>**Black level**: The reference value the sensor outputs even when there is no light at all. The first stage of ISP processing subtracts this value.
- <a id="d1-term-셰이더"></a>**Shader**: A small program that runs on the GPU. A software ISP may perform debayering and color correction with GPU shaders.
- **Software ISP**: A libcamera component that performs ISP processing on the CPU or GPU in place of a hardware ISP on devices without one. In the source, it is named software_isp or softisp.
- <a id="d1-term-왜곡-보정"></a>**Distortion correction**: A process that straightens an image bent by the lens. The RKISP1 pipeline performs it by supplying a vertex map to the DW100 device.
- <a id="d1-term-컨트롤-정보-맵"></a>**Control information map**: Information that indicates the control items and ranges to be used with the camera. The control list of a request must refer to that camera's information map.
- <a id="d1-term-튜닝-파일"></a>**Tuning file**: A YAML file containing sensor- and platform-specific algorithm parameters (calibration tables, color matrices, etc.). IPA reads it when it starts.
- <a id="d1-term-프레임-버퍼"></a>**Frame buffer**: A FrameBuffer object that represents the memory region storing image data. It provides the file descriptor, offset, and length of each memory plane, along with per-frame metadata. The valid scope of the data and metadata differs depending on whether capture succeeds, fails, or is canceled.
- **Proxy**: A proxy object that does not call the IPA module directly. It receives calls through the same interface and forwards them to an IPA thread or a separate process. It is automatically generated from mojom definitions at build time.
- <a id="d1-term-활성-스트림"></a>**Active streams**: A Stream connected to the current camera configuration. If a request buffer refers to a stream of a different configuration, the submission check rejects it.

## Source manuscripts and review records

<details open>
<summary>Glossary</summary>

- **Contracts between documents**: [Automated comparison report](https://ttolsun.github.io/libcamera-sdd/contract-consistency.json) · Before human review

[Open earlier detail](https://ttolsun.github.io/libcamera-sdd/en/reader-archive/glossary.html#page-evidence)

</details>

[Download page Markdown](https://ttolsun.github.io/libcamera-sdd/en/glossary.md) · [Reader edition source map](https://ttolsun.github.io/libcamera-sdd/reader-edition.json)
