---
generated_at: 2026-10-26T11:47:39+00:00
source_commit: 960713a8f9b404bb64ce9b05d1ffd5df7e84dd05
status: ok
section: component-index
generation_method: extracted-structure
evidence_fingerprint: 7a654e15cb9a6570319e50c4d927720d9d87da234ae0dff3399e4d05485fae74
semantic_review: human-review-required
---

# 구성 요소 색인

**빌드한 모든 파이프라인·IPA·앱의 클래스와 함수를 패키지별로 찾으세요. 표는 추출 사실에서 만들었고 동작은 설명하지 않습니다.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| include/libcamera 절을 확인합니다. | [include/libcamera](#includelibcamera) |
| include/libcamera/base 절을 확인합니다. | [include/libcamera/base](#includelibcamerabase) |
| include/libcamera/internal 절을 확인합니다. | [include/libcamera/internal](#includelibcamerainternal) |
| include/libcamera/ipa 절을 확인합니다. | [include/libcamera/ipa](#includelibcameraipa) |
| src/apps/cam 절을 확인합니다. | [src/apps/cam](#srcappscam) |
| src/apps/common 절을 확인합니다. | [src/apps/common](#srcappscommon) |

## include/libcamera

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::Camera` | `include/libcamera/camera.h:114` | `libcamera::Object`, `libcamera::Extensible` | Camera device |
| `libcamera::CameraConfiguration` | `include/libcamera/camera.h:60` | – | Hold configuration for streams of the camera |
| `libcamera::CameraConfiguration::ColorSpaceFlag` | `include/libcamera/camera.h:102` | – | 확인 필요 |
| `libcamera::CameraConfiguration::Status` | `include/libcamera/camera.h:63` | – | 확인 필요 |
| `libcamera::CameraManager` | `include/libcamera/camera_manager.h:24` | `libcamera::Object`, `libcamera::Extensible` | Provide access and manage all cameras in the system |
| `libcamera::ColorSpace` | `include/libcamera/color_space.h:17` | – | Class to describe a color space |
| `libcamera::ColorSpace::Primaries` | `include/libcamera/color_space.h:20` | – | 확인 필요 |
| `libcamera::ColorSpace::Range` | `include/libcamera/color_space.h:40` | – | 확인 필요 |
| `libcamera::ColorSpace::TransferFunction` | `include/libcamera/color_space.h:27` | – | 확인 필요 |
| `libcamera::ColorSpace::YcbcrEncoding` | `include/libcamera/color_space.h:33` | – | 확인 필요 |
| `libcamera::Control` | `include/libcamera/controls.h:356` | `libcamera::ControlId` | Describe a control and its intrinsic properties |
| `libcamera::ControlId` | `include/libcamera/controls.h:294` | – | Control static metadata |
| `libcamera::ControlId::Direction` | `include/libcamera/controls.h:297` | – | 확인 필요 |
| `libcamera::ControlInfo` | `include/libcamera/controls.h:373` | – | Describe the limits of valid values for a Control |
| `libcamera::ControlInfoMap` | `include/libcamera/controls.h:408` | – | A map of ControlId to ControlInfo |
| `libcamera::ControlList` | `include/libcamera/controls.h:452` | – | Associate a list of ControlId with their values for an object |
| `libcamera::ControlList::MergePolicy` | `include/libcamera/controls.h:458` | – | 확인 필요 |
| `libcamera::ControlType` | `include/libcamera/controls.h:30` | – | 확인 필요 |
| `libcamera::ControlValue` | `include/libcamera/controls.h:142` | – | Abstract type representing the value of a control |
| `libcamera::Fence` | `include/libcamera/fence.h:15` | – | Synchronization primitive to manage resources |
| `libcamera::FrameBuffer` | `include/libcamera/framebuffer.h:49` | `libcamera::Extensible` | Frame buffer data and its associated dynamic metadata |
| `libcamera::FrameBuffer::Plane` | `include/libcamera/framebuffer.h:54` | – | 확인 필요 |
| `libcamera::FrameBufferAllocator` | `include/libcamera/framebuffer_allocator.h:22` | – | FrameBuffer allocator for applications |
| `libcamera::FrameMetadata` | `include/libcamera/framebuffer.h:24` | – | Metadata related to a captured frame |
| `libcamera::FrameMetadata::Plane` | `include/libcamera/framebuffer.h:32` | – | Per-plane frame metadata |
| `libcamera::FrameMetadata::Status` | `include/libcamera/framebuffer.h:25` | – | 확인 필요 |
| `libcamera::LoggingTarget` | `include/libcamera/logging.h:14` | – | 확인 필요 |
| `libcamera::Orientation` | `include/libcamera/orientation.h:15` | – | 확인 필요 |
| `libcamera::PixelFormat` | `include/libcamera/pixel_format.h:16` | – | libcamera image pixel format |
| `libcamera::Point` | `include/libcamera/geometry.h:18` | – | Describe a point in two-dimensional space |
| `libcamera::Rectangle` | `include/libcamera/geometry.h:246` | – | Describe a rectangle's position and dimensions |
| `libcamera::Request` | `include/libcamera/request.h:29` | `libcamera::Extensible` | A frame capture request |
| `libcamera::Request::ReuseFlag` | `include/libcamera/request.h:40` | – | 확인 필요 |
| `libcamera::Request::Status` | `include/libcamera/request.h:34` | – | 확인 필요 |
| `libcamera::SensorConfiguration` | `include/libcamera/camera.h:36` | – | Camera sensor configuration |
| `libcamera::SensorConfiguration::(unnamed struct at include/libcamera/camera.h:43:2)` | `include/libcamera/camera.h:43` | – | 확인 필요 |
| `libcamera::SensorConfiguration::(unnamed struct at include/libcamera/camera.h:48:2)` | `include/libcamera/camera.h:48` | – | 확인 필요 |
| `libcamera::Size` | `include/libcamera/geometry.h:50` | – | Describe a two-dimensional size |
| `libcamera::SizeRange` | `include/libcamera/geometry.h:204` | – | Describe a range of sizes |
| `libcamera::Stream` | `include/libcamera/stream.h:75` | – | Video stream for a camera |
| `libcamera::StreamConfiguration` | `include/libcamera/stream.h:40` | – | Configuration parameters for a stream |
| `libcamera::StreamFormats` | `include/libcamera/stream.h:25` | – | Hold information about supported stream formats |
| `libcamera::StreamRole` | `include/libcamera/stream.h:66` | – | 확인 필요 |
| `libcamera::Transform` | `include/libcamera/transform.h:16` | – | 확인 필요 |
| `libcamera::details::control_type` | `include/libcamera/controls.h:56` | – | 확인 필요 |
| `libcamera::details::is_span` | `include/libcamera/controls.h:48` | – | 확인 필요 |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::logSetFile` | `include/libcamera/logging.h:21` | `src/libcamera/base/log.cpp:374` | Direct logging to a file |
| `libcamera::logSetLevel` | `include/libcamera/logging.h:24` | `src/libcamera/base/log.cpp:440` | Set the log level |
| `libcamera::logSetStream` | `include/libcamera/logging.h:22` | `src/libcamera/base/log.cpp:397` | Direct logging to a stream |
| `libcamera::logSetTarget` | `include/libcamera/logging.h:23` | `src/libcamera/base/log.cpp:420` | Set the logging target |
| `libcamera::operator!` | – | `include/libcamera/transform.h:63` | 확인 필요 |
| `libcamera::operator&=` | – | `include/libcamera/transform.h:44` | 확인 필요 |
| `libcamera::operator*` | `include/libcamera/transform.h:59` | `src/libcamera/transform.cpp:209` | Compose two transforms by applying t0 first then t1 |
| `libcamera::operator-` | `include/libcamera/transform.h:61` | `src/libcamera/transform.cpp:235` | Invert a transform |
| `libcamera::operator/` | `include/libcamera/transform.h:75` | `src/libcamera/transform.cpp:343` | Return the Transform that applied to o2 gives o1 |
| `libcamera::operator<` | `include/libcamera/geometry.h:180` | `src/libcamera/geometry.cpp:411` | Compare sizes for smaller than order |
| `libcamera::operator<<` | `include/libcamera/geometry.h:48` | `src/libcamera/geometry.cpp:93` | Insert a text representation of a Point into an output stream |
| `libcamera::operator<=` | – | `include/libcamera/geometry.h:187` | 확인 필요 |
| `libcamera::operator==` | `include/libcamera/geometry.h:42` | `include/libcamera/base/shared_fd.h:49` | Compare color spaces for equality |
| `libcamera::operator>` | – | `include/libcamera/geometry.h:192` | 확인 필요 |
| `libcamera::operator>=` | – | `include/libcamera/geometry.h:197` | 확인 필요 |
| `libcamera::operator^=` | – | `include/libcamera/transform.h:54` | 확인 필요 |
| `libcamera::operator|=` | – | `include/libcamera/transform.h:49` | 확인 필요 |
| `libcamera::orientationFromRotation` | `include/libcamera/orientation.h:27` | `src/libcamera/orientation.cpp:70` | Return the orientation representing a rotation of the given angle clockwise |
| `libcamera::transformFromRotation` | `include/libcamera/transform.h:73` | `src/libcamera/transform.cpp:280` | Return the transform representing a rotation of the given angle clockwise |
| `libcamera::transformToString` | `include/libcamera/transform.h:78` | `src/libcamera/transform.cpp:389` | Return a character string describing the transform |

## include/libcamera/base

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::Backtrace` | `include/libcamera/base/backtrace.h:19` | – | Representation of a call stack backtrace |
| `libcamera::BoundMethodArgs` | `include/libcamera/base/bound_method.h:88` | `libcamera::BoundMethodBase` | 확인 필요 |
| `libcamera::BoundMethodBase` | `include/libcamera/base/bound_method.h:59` | – | 확인 필요 |
| `libcamera::BoundMethodFunctor` | `include/libcamera/base/bound_method.h:113` | `libcamera::BoundMethodArgs` | 확인 필요 |
| `libcamera::BoundMethodMember` | `include/libcamera/base/bound_method.h:146` | `libcamera::BoundMethodArgs` | 확인 필요 |
| `libcamera::BoundMethodPack` | `include/libcamera/base/bound_method.h:33` | `libcamera::BoundMethodPackBase` | 확인 필요 |
| `libcamera::BoundMethodPackBase` | `include/libcamera/base/bound_method.h:26` | – | 확인 필요 |
| `libcamera::BoundMethodStatic` | `include/libcamera/base/bound_method.h:184` | `libcamera::BoundMethodArgs` | 확인 필요 |
| `libcamera::ConditionVariable` | `include/libcamera/base/mutex.h:80` | – | std::condition_variable wrapper integrating with MutexLocker |
| `libcamera::ConnectionType` | `include/libcamera/base/bound_method.h:19` | – | 확인 필요 |
| `libcamera::EventDispatcher` | `include/libcamera/base/event_dispatcher.h:17` | – | Interface to manage the libcamera events and timers |
| `libcamera::EventDispatcherPoll` | `include/libcamera/base/event_dispatcher_poll.h:26` | `libcamera::EventDispatcher` | A poll-based event dispatcher |
| `libcamera::EventDispatcherPoll::EventNotifierSetPoll` | `include/libcamera/base/event_dispatcher_poll.h:42` | – | 확인 필요 |
| `libcamera::EventNotifier` | `include/libcamera/base/event_notifier.h:19` | `libcamera::Object` | Notify of activity on a file descriptor |
| `libcamera::EventNotifier::Type` | `include/libcamera/base/event_notifier.h:22` | – | 확인 필요 |
| `libcamera::Extensible` | `include/libcamera/base/class.h:61` | – | Base class to manage private data through a d-pointer |
| `libcamera::Extensible::Private` | `include/libcamera/base/class.h:64` | – | Base class for private data managed through a d-pointer |
| `libcamera::File` | `include/libcamera/base/file.h:24` | – | Interface for I/O operations on files |
| `libcamera::File::MapFlag` | `include/libcamera/base/file.h:27` | – | 확인 필요 |
| `libcamera::File::OpenModeFlag` | `include/libcamera/base/file.h:34` | – | 확인 필요 |
| `libcamera::Flags` | `include/libcamera/base/flags.h:15` | – | Type-safe container for enum-based bitfields |
| `libcamera::InvokeMessage` | `include/libcamera/base/message.h:51` | `libcamera::Message` | A message carrying a method invocation across threads |
| `libcamera::LogCategory` | `include/libcamera/base/log.h:30` | – | A category of log message |
| `libcamera::LogMessage` | `include/libcamera/base/log.h:63` | – | Internal log message representation. |
| `libcamera::LogMessageAbortGuard` | `include/libcamera/base/log.h:93` | – | 확인 필요 |
| `libcamera::LogSeverity` | `include/libcamera/base/log.h:21` | – | 확인 필요 |
| `libcamera::Loggable` | `include/libcamera/base/log.h:104` | – | Base class to support log message extensions |
| `libcamera::MemFd` | `include/libcamera/base/memfd.h:17` | – | Helper class to create anonymous files |
| `libcamera::MemFd::Seal` | `include/libcamera/base/memfd.h:20` | – | 확인 필요 |
| `libcamera::Message` | `include/libcamera/base/message.h:23` | – | A message that can be posted to a Thread |
| `libcamera::Message::Type` | `include/libcamera/base/message.h:26` | – | 확인 필요 |
| `libcamera::Mutex` | `include/libcamera/base/mutex.h:23` | – | std::mutex wrapper with clang thread safety annotation |
| `libcamera::MutexLocker` | `include/libcamera/base/mutex.h:42` | – | std::unique_lock wrapper with clang thread safety annotation |
| `libcamera::Object` | `include/libcamera/base/object.h:26` | – | Base object to support automatic signal disconnection |
| `libcamera::Semaphore` | `include/libcamera/base/semaphore.h:16` | – | General-purpose counting semaphore |
| `libcamera::SharedFD` | `include/libcamera/base/shared_fd.h:16` | – | RAII-style wrapper for file descriptors |
| `libcamera::SharedFD::Descriptor` | `include/libcamera/base/shared_fd.h:34` | – | 확인 필요 |
| `libcamera::Signal` | `include/libcamera/base/signal.h:38` | `libcamera::SignalBase` | Generic signal and slot communication mechanism |
| `libcamera::SignalBase` | `include/libcamera/base/signal.h:20` | – | 확인 필요 |
| `libcamera::Thread` | `include/libcamera/base/thread.h:31` | – | A thread of execution |
| `libcamera::Timer` | `include/libcamera/base/timer.h:21` | `libcamera::Object` | Single-shot timer interface |
| `libcamera::UniqueFD` | `include/libcamera/base/unique_fd.h:16` | – | unique_ptr-like wrapper for a file descriptor |
| `libcamera::flags_enable_operators` | `include/libcamera/base/flags.h:145` | – | 확인 필요 |
| `libcamera::utils::Duration` | `include/libcamera/base/utils.h:330` | – | Helper class from std::chrono::duration that represents a time |
| `libcamera::utils::ScopeExitActions` | `include/libcamera/base/utils.h:384` | – | An object that performs actions upon destruction |
| `libcamera::utils::details::StringSplitter` | `include/libcamera/base/utils.h:158` | – | 확인 필요 |
| `libcamera::utils::details::StringSplitter::iterator` | `include/libcamera/base/utils.h:163` | – | 확인 필요 |
| `libcamera::utils::details::defopt_t` | `include/libcamera/base/utils.h:435` | – | 확인 필요 |
| `libcamera::utils::details::enumerate_adapter` | `include/libcamera/base/utils.h:297` | – | 확인 필요 |
| `libcamera::utils::details::enumerate_iterator` | `include/libcamera/base/utils.h:257` | – | 확인 필요 |
| `libcamera::utils::details::hex` | `include/libcamera/base/utils.h:91` | – | 확인 필요 |
| `libcamera::utils::details::reverse_adapter` | `include/libcamera/base/utils.h:230` | – | 확인 필요 |
| `libcamera::utils::overloaded` | `include/libcamera/base/utils.h:41` | – | Helper type for type-matching std::visit() implementations |
| `libcamera::utils::scope_exit` | `include/libcamera/base/utils.h:398` | – | 확인 필요 |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::_log` | `include/libcamera/base/log.h:117` | `src/libcamera/base/log.cpp:987` | Create a temporary LogMessage object to log a message |
| `libcamera::isLogSeverityEnabled` | – | `include/libcamera/base/log.h:126` | Returns `int` to avoid `-Wswitch-bool` below. |
| `libcamera::operator!=` | – | `include/libcamera/base/shared_fd.h:54` | 확인 필요 |
| `libcamera::operator&` | – | `include/libcamera/base/flags.h:159` | 확인 필요 |
| `libcamera::operator^` | – | `include/libcamera/base/flags.h:167` | 확인 필요 |
| `libcamera::operator|` | – | `include/libcamera/base/flags.h:151` | 확인 필요 |
| `libcamera::operator~` | – | `include/libcamera/base/flags.h:175` | 확인 필요 |
| `libcamera::utils::<deduction guide for overloaded>` | `include/libcamera/base/utils.h:46` | – | 확인 필요 |
| `libcamera::utils::<deduction guide for scope_exit>` | `include/libcamera/base/utils.h:429` | – | 확인 필요 |
| `libcamera::utils::__xpg_basename` | `include/libcamera/base/utils.h:49` | – | 확인 필요 |
| `libcamera::utils::abs_diff` | – | `include/libcamera/base/utils.h:368` | 확인 필요 |
| `libcamera::utils::alignDown` | – | `include/libcamera/base/utils.h:217` | 확인 필요 |
| `libcamera::utils::alignUp` | – | `include/libcamera/base/utils.h:222` | 확인 필요 |
| `libcamera::utils::basename` | `include/libcamera/base/utils.h:49` | `src/libcamera/base/utils.cpp:67` | Strip the directory prefix from the path |
| `libcamera::utils::details::begin` | – | `include/libcamera/base/utils.h:235` | 확인 필요 |
| `libcamera::utils::details::end` | – | `include/libcamera/base/utils.h:241` | 확인 필요 |
| `libcamera::utils::details::hex_width` | – | `include/libcamera/base/utils.h:97` | 확인 필요 |
| `libcamera::utils::details::operator<<` | `include/libcamera/base/utils.h:103` | `src/libcamera/base/utils.cpp:220` | 확인 필요 |
| `libcamera::utils::dirname` | `include/libcamera/base/utils.h:52` | `src/libcamera/base/utils.cpp:113` | Identify the dirname portion of a path |
| `libcamera::utils::duration_to_timespec` | `include/libcamera/base/utils.h:86` | `src/libcamera/base/utils.cpp:191` | Convert a duration to a timespec |
| `libcamera::utils::enumerate` | – | `include/libcamera/base/utils.h:325` | 확인 필요 |
| `libcamera::utils::hex` | – | `include/libcamera/base/utils.h:108` | 확인 필요 |
| `libcamera::utils::join` | – | `include/libcamera/base/utils.h:117` | 확인 필요 |
| `libcamera::utils::libcameraBuildPath` | `include/libcamera/base/utils.h:214` | `src/libcamera/source_paths.cpp:74` | Retrieve the path to the build directory |
| `libcamera::utils::libcameraSourcePath` | `include/libcamera/base/utils.h:215` | `src/libcamera/source_paths.cpp:114` | Retrieve the path to the source directory |
| `libcamera::utils::map_keys` | – | `include/libcamera/base/utils.h:55` | 확인 필요 |
| `libcamera::utils::operator<<` | `include/libcamera/base/utils.h:449` | `src/libcamera/base/utils.cpp:706` | 확인 필요 |
| `libcamera::utils::reverse` | – | `include/libcamera/base/utils.h:249` | 확인 필요 |
| `libcamera::utils::secure_getenv` | `include/libcamera/base/utils.h:51` | `src/libcamera/base/utils.cpp:91` | Get an environment variable |
| `libcamera::utils::set_overlap` | – | `include/libcamera/base/utils.h:64` | 확인 필요 |
| `libcamera::utils::split` | `include/libcamera/base/utils.h:210` | `src/libcamera/base/utils.cpp:339` | Split a string based on a delimiter |
| `libcamera::utils::strlcpy` | `include/libcamera/base/utils.h:113` | `src/libcamera/base/utils.cpp:271` | Copy a string with a size limit |
| `libcamera::utils::strtod` | `include/libcamera/base/utils.h:376` | `src/libcamera/base/utils.cpp:533` | Convert a string to a double independently of the current locale |
| `libcamera::utils::time_point_to_string` | `include/libcamera/base/utils.h:87` | `src/libcamera/base/utils.cpp:205` | Convert a time point to a string representation |
| `libcamera::utils::toAscii` | `include/libcamera/base/utils.h:212` | `src/libcamera/base/utils.cpp:353` | Remove any non-ASCII characters from a string |
| `libcamera::utils::to_underlying` | – | `include/libcamera/base/utils.h:379` | 확인 필요 |

## include/libcamera/internal

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::BayerFormat` | `include/libcamera/internal/bayer_format.h:22` | – | Class to represent a raw image Bayer format |
| `libcamera::BayerFormat::Order` | `include/libcamera/internal/bayer_format.h:25` | – | 확인 필요 |
| `libcamera::BayerFormat::Packing` | `include/libcamera/internal/bayer_format.h:33` | – | 확인 필요 |
| `libcamera::Benchmark` | `include/libcamera/internal/software_isp/benchmark.h:21` | – | Simple builtin benchmark |
| `libcamera::ByteStreamBuffer` | `include/libcamera/internal/byte_stream_buffer.h:19` | – | Wrap a memory buffer and provide sequential data read and write |
| `libcamera::Camera::Private` | `include/libcamera/internal/camera.h:28` | `libcamera::Extensible::Private` | Base class for camera private data |
| `libcamera::Camera::Private::State` | `include/libcamera/internal/camera.h:49` | – | 확인 필요 |
| `libcamera::CameraControlValidator` | `include/libcamera/internal/camera_controls.h:16` | `libcamera::ControlValidator` | A control validator for Camera instances |
| `libcamera::CameraLens` | `include/libcamera/internal/camera_lens.h:23` | `libcamera::Loggable` | A camera lens based on V4L2 subdevices |
| `libcamera::CameraManager::Private` | `include/libcamera/internal/camera_manager.h:31` | `libcamera::Extensible::Private`, `libcamera::Thread` | 확인 필요 |
| `libcamera::CameraSensor` | `include/libcamera/internal/camera_sensor.h:39` | – | A abstract camera sensor |
| `libcamera::CameraSensorFactory` | `include/libcamera/internal/camera_sensor.h:114` | `libcamera::CameraSensorFactoryBase` | Registration of CameraSensorFactory classes and creation of instances |
| `libcamera::CameraSensorFactoryBase` | `include/libcamera/internal/camera_sensor.h:88` | – | Base class for camera sensor factories |
| `libcamera::CameraSensorProperties` | `include/libcamera/internal/camera_sensor_properties.h:19` | – | Database of camera sensor properties |
| `libcamera::CameraSensorProperties::SensorDelays` | `include/libcamera/internal/camera_sensor_properties.h:20` | – | Sensor control application delay values |
| `libcamera::ClockRecovery` | `include/libcamera/internal/clock_recovery.h:13` | – | Recover an output clock from an input clock |
| `libcamera::ControlSerializer` | `include/libcamera/internal/control_serializer.h:20` | – | Serializer and deserializer for control-related classes |
| `libcamera::ControlSerializer::Role` | `include/libcamera/internal/control_serializer.h:23` | – | 확인 필요 |
| `libcamera::ControlValidator` | `include/libcamera/internal/control_validator.h:16` | – | Interface for the control validator |
| `libcamera::Converter` | `include/libcamera/internal/converter.h:35` | – | Abstract Base Class for converter |
| `libcamera::Converter::Alignment` | `include/libcamera/internal/converter.h:45` | – | 확인 필요 |
| `libcamera::Converter::Feature` | `include/libcamera/internal/converter.h:38` | – | 확인 필요 |
| `libcamera::ConverterDW100Module` | `include/libcamera/internal/converter/converter_dw100.h:28` | – | A converter module for the dw100 dewarper |
| `libcamera::ConverterDW100Module::VertexMapInfo` | `include/libcamera/internal/converter/converter_dw100.h:74` | – | 확인 필요 |
| `libcamera::ConverterFactory` | `include/libcamera/internal/converter.h:129` | `libcamera::ConverterFactoryBase` | Registration of ConverterFactory classes and creation of instances |
| `libcamera::ConverterFactoryBase` | `include/libcamera/internal/converter.h:104` | – | Base class for converter factories |
| `libcamera::DebayerParams` | `include/libcamera/internal/software_isp/debayer_params.h:21` | – | Struct to hold the debayer parameters. |
| `libcamera::DebugMetadata` | `include/libcamera/internal/debug_controls.h:14` | – | Helper to record metadata for later use |
| `libcamera::DelayedControls` | `include/libcamera/internal/delayed_controls.h:22` | `libcamera::Object` | Helper to deal with controls that take effect with a delay |
| `libcamera::DelayedControls::ControlParams` | `include/libcamera/internal/delayed_controls.h:25` | – | 확인 필요 |
| `libcamera::DelayedControls::ControlRingBuffer` | `include/libcamera/internal/delayed_controls.h:59` | – | 확인 필요 |
| `libcamera::DelayedControls::Info` | `include/libcamera/internal/delayed_controls.h:41` | `libcamera::ControlValue` | 확인 필요 |
| `libcamera::DeviceEnumerator` | `include/libcamera/internal/device_enumerator.h:37` | – | Enumerate, store and search media devices |
| `libcamera::DeviceEnumeratorSysfs` | `include/libcamera/internal/device_enumerator_sysfs.h:18` | `libcamera::DeviceEnumerator` | 확인 필요 |
| `libcamera::DeviceEnumeratorUdev` | `include/libcamera/internal/device_enumerator_udev.h:32` | `libcamera::DeviceEnumerator` | 확인 필요 |
| `libcamera::DeviceEnumeratorUdev::MediaDeviceDeps` | `include/libcamera/internal/device_enumerator_udev.h:44` | – | 확인 필요 |
| `libcamera::DeviceMatch` | `include/libcamera/internal/device_enumerator.h:21` | – | Description of a media device search pattern |
| `libcamera::DmaBufAllocator` | `include/libcamera/internal/dma_buf_allocator.h:23` | – | Helper class for dma-buf allocations |
| `libcamera::DmaBufAllocator::DmaBufAllocatorFlag` | `include/libcamera/internal/dma_buf_allocator.h:26` | – | 확인 필요 |
| `libcamera::DmaSyncer` | `include/libcamera/internal/dma_buf_allocator.h:53` | – | Helper class for dma-buf's synchronization |
| `libcamera::DmaSyncer::SyncType` | `include/libcamera/internal/dma_buf_allocator.h:56` | – | 확인 필요 |
| `libcamera::Dw100VertexMap` | `include/libcamera/internal/converter/converter_dw100_vertexmap.h:25` | – | Helper class to compute dw100 vertex maps |
| `libcamera::Dw100VertexMap::DewarpParams` | `include/libcamera/internal/converter/converter_dw100_vertexmap.h:33` | – | Structure combining all dewarp parameters |
| `libcamera::Dw100VertexMap::DewarpParams::(unnamed struct at include/libcamera/internal/converter/converter_dw100_vertexmap.h:46:3)` | `include/libcamera/internal/converter/converter_dw100_vertexmap.h:46` | – | 확인 필요 |
| `libcamera::Dw100VertexMap::ScaleMode` | `include/libcamera/internal/converter/converter_dw100_vertexmap.h:28` | – | 확인 필요 |
| `libcamera::FrameBuffer::Private` | `include/libcamera/internal/framebuffer.h:22` | `libcamera::Extensible::Private` | Base class for FrameBuffer private data |
| `libcamera::GlobalConfiguration` | `include/libcamera/internal/global_configuration.h:22` | – | Support for global libcamera configuration |
| `libcamera::IPADataSerializer` | `include/libcamera/internal/ipa_data_serializer.h:65` | – | IPA Data Serializer |
| `libcamera::IPAManager` | `include/libcamera/internal/ipa_manager.h:29` | – | Manager for IPA modules |
| `libcamera::IPAModule` | `include/libcamera/internal/ipa_module.h:21` | `libcamera::Loggable` | Wrapper around IPA module shared object |
| `libcamera::IPAProxy` | `include/libcamera/internal/ipa_proxy.h:22` | `libcamera::IPAInterface` | IPA Proxy |
| `libcamera::IPAProxy::ProxyState` | `include/libcamera/internal/ipa_proxy.h:25` | – | 확인 필요 |
| `libcamera::IPCMessage` | `include/libcamera/internal/ipc_pipe.h:20` | – | IPC message to be passed through IPC message pipe |
| `libcamera::IPCMessage::Header` | `include/libcamera/internal/ipc_pipe.h:23` | – | Container for an IPCMessage header |
| `libcamera::IPCPipe` | `include/libcamera/internal/ipc_pipe.h:50` | – | IPC message pipe for IPA isolation |
| `libcamera::IPCPipeUnixSocket` | `include/libcamera/internal/ipc_pipe_unixsocket.h:21` | `libcamera::IPCPipe` | 확인 필요 |
| `libcamera::IPCPipeUnixSocket::CallData` | `include/libcamera/internal/ipc_pipe_unixsocket.h:33` | – | 확인 필요 |
| `libcamera::IPCUnixSocket` | `include/libcamera/internal/ipc_unixsocket.h:22` | – | IPC mechanism based on Unix sockets |
| `libcamera::IPCUnixSocket::Header` | `include/libcamera/internal/ipc_unixsocket.h:44` | – | 확인 필요 |
| `libcamera::IPCUnixSocket::Payload` | `include/libcamera/internal/ipc_unixsocket.h:25` | – | Container for an IPC payload |
| `libcamera::MappedBuffer` | `include/libcamera/internal/mapped_framebuffer.h:21` | – | Provide an interface to support managing memory mapped buffers |
| `libcamera::MappedFrameBuffer` | `include/libcamera/internal/mapped_framebuffer.h:46` | `libcamera::MappedBuffer` | Map a FrameBuffer using the MappedBuffer interface |
| `libcamera::MappedFrameBuffer::MapFlag` | `include/libcamera/internal/mapped_framebuffer.h:49` | – | 확인 필요 |
| `libcamera::Matrix` | `include/libcamera/internal/matrix.h:30` | – | Matrix class |
| `libcamera::MediaBusFormatInfo` | `include/libcamera/internal/v4l2_subdevice.h:34` | – | Information about media bus formats |
| `libcamera::MediaBusFormatInfo::Type` | `include/libcamera/internal/v4l2_subdevice.h:37` | – | 확인 필요 |
| `libcamera::MediaDevice` | `include/libcamera/internal/media_device.h:27` | `libcamera::Loggable` | The MediaDevice represents a Media Controller device with its full |
| `libcamera::MediaEntity` | `include/libcamera/internal/media_object.h:96` | `libcamera::MediaObject` | The MediaEntity represents an entity in the media graph |
| `libcamera::MediaEntity::Type` | `include/libcamera/internal/media_object.h:99` | – | 확인 필요 |
| `libcamera::MediaLink` | `include/libcamera/internal/media_object.h:43` | `libcamera::MediaObject` | The MediaLink represents a link between two pads in the media graph. |
| `libcamera::MediaObject` | `include/libcamera/internal/media_object.h:23` | – | Base class for all media objects |
| `libcamera::MediaPad` | `include/libcamera/internal/media_object.h:68` | `libcamera::MediaObject` | The MediaPad represents a pad of an entity in the media graph |
| `libcamera::MediaPipeline` | `include/libcamera/internal/media_pipeline.h:23` | – | The MediaPipeline represents a set of entities that together form a |
| `libcamera::MediaPipeline::Entity` | `include/libcamera/internal/media_pipeline.h:26` | – | A node composing the media pipeline |
| `libcamera::PipelineHandler` | `include/libcamera/internal/pipeline_handler.h:34` | `libcamera::Object` | Create and manage cameras based on a set of media devices |
| `libcamera::PipelineHandlerFactory` | `include/libcamera/internal/pipeline_handler.h:144` | `libcamera::PipelineHandlerFactoryBase` | Registration of PipelineHandler classes and creation of instances |
| `libcamera::PipelineHandlerFactoryBase` | `include/libcamera/internal/pipeline_handler.h:121` | – | Base class for pipeline handler factories |
| `libcamera::PixelFormatInfo` | `include/libcamera/internal/formats.h:20` | – | Information about pixel formats |
| `libcamera::PixelFormatInfo::ColourEncoding` | `include/libcamera/internal/formats.h:23` | – | 확인 필요 |
| `libcamera::PixelFormatInfo::Plane` | `include/libcamera/internal/formats.h:29` | – | Information about a single plane of a pixel format |
| `libcamera::Process` | `include/libcamera/internal/process.h:22` | – | Process object |
| `libcamera::Process::ExitStatus` | `include/libcamera/internal/process.h:25` | – | 확인 필요 |
| `libcamera::PubKey` | `include/libcamera/internal/pub_key.h:21` | – | Public key wrapper for signature verification |
| `libcamera::Request::Private` | `include/libcamera/internal/request.h:28` | `libcamera::Extensible::Private` | Request private data |
| `libcamera::SharedMem` | `include/libcamera/internal/shared_mem_object.h:23` | – | Helper class to allocate and manage memory shareable between processes |
| `libcamera::SharedMemObject` | `include/libcamera/internal/shared_mem_object.h:59` | `libcamera::SharedMem` | Helper class to allocate an object in shareable memory |
| `libcamera::SoftwareIsp` | `include/libcamera/internal/software_isp/software_isp.h:47` | `libcamera::Object` | Class for the Software ISP |
| `libcamera::SwIspStats` | `include/libcamera/internal/software_isp/swisp_stats.h:24` | – | Struct that holds the statistics for the Software ISP |
| `libcamera::SwStatsCpu` | `include/libcamera/internal/software_isp/swstats_cpu.h:35` | – | Class for gathering statistics on the CPU |
| `libcamera::V4L2BufferCache` | `include/libcamera/internal/v4l2_videodevice.h:124` | – | Hot cache of associations between V4L2 buffer indexes and FrameBuffer |
| `libcamera::V4L2BufferCache::Entry` | `include/libcamera/internal/v4l2_videodevice.h:136` | – | 확인 필요 |
| `libcamera::V4L2BufferCache::Entry::Plane` | `include/libcamera/internal/v4l2_videodevice.h:148` | – | 확인 필요 |
| `libcamera::V4L2Capability` | `include/libcamera/internal/v4l2_videodevice.h:44` | `v4l2_capability` | struct v4l2_capability object wrapper and helpers |
| `libcamera::V4L2Device` | `include/libcamera/internal/v4l2_device.h:33` | `libcamera::Loggable` | Base class for V4L2VideoDevice and V4L2Subdevice |
| `libcamera::V4L2DeviceFormat` | `include/libcamera/internal/v4l2_videodevice.h:167` | – | The V4L2 video device image format and sizes |
| `libcamera::V4L2DeviceFormat::Plane` | `include/libcamera/internal/v4l2_videodevice.h:170` | – | Per-plane memory size information |
| `libcamera::V4L2M2MConverter` | `include/libcamera/internal/converter/converter_v4l2_m2m.h:37` | `libcamera::Converter` | The V4L2 M2M converter implements the converter interface based on |
| `libcamera::V4L2M2MConverter::V4L2M2MStream` | `include/libcamera/internal/converter/converter_v4l2_m2m.h:85` | `libcamera::Loggable` | 확인 필요 |
| `libcamera::V4L2M2MDevice` | `include/libcamera/internal/v4l2_videodevice.h:295` | – | Memory-to-Memory video device |
| `libcamera::V4L2PixelFormat` | `include/libcamera/internal/v4l2_pixelformat.h:23` | – | V4L2 pixel format FourCC wrapper |
| `libcamera::V4L2PixelFormat::Info` | `include/libcamera/internal/v4l2_pixelformat.h:26` | – | Information about a V4L2 pixel format |
| `libcamera::V4L2Request` | `include/libcamera/internal/v4l2_request.h:21` | `libcamera::Loggable` | V4L2Request object and API |
| `libcamera::V4L2Subdevice` | `include/libcamera/internal/v4l2_subdevice.h:75` | `libcamera::V4L2Device` | A V4L2 subdevice as exposed by the Linux kernel |
| `libcamera::V4L2Subdevice::Route` | `include/libcamera/internal/v4l2_subdevice.h:100` | – | V4L2 subdevice routing table entry |
| `libcamera::V4L2Subdevice::Stream` | `include/libcamera/internal/v4l2_subdevice.h:85` | – | V4L2 subdevice stream |
| `libcamera::V4L2Subdevice::Whence` | `include/libcamera/internal/v4l2_subdevice.h:80` | – | 확인 필요 |
| `libcamera::V4L2SubdeviceCapability` | `include/libcamera/internal/v4l2_subdevice.h:54` | `v4l2_subdev_capability` | struct v4l2_subdev_capability object wrapper and helpers |
| `libcamera::V4L2SubdeviceFormat` | `include/libcamera/internal/v4l2_subdevice.h:65` | – | The V4L2 sub-device image format and sizes |
| `libcamera::V4L2VideoDevice` | `include/libcamera/internal/v4l2_videodevice.h:187` | `libcamera::V4L2Device` | V4L2VideoDevice object and API |
| `libcamera::V4L2VideoDevice::State` | `include/libcamera/internal/v4l2_videodevice.h:241` | – | 확인 필요 |
| `libcamera::ValueNode` | `include/libcamera/internal/value_node.h:26` | – | A class representing a tree structure of values |
| `libcamera::ValueNode::Accessor` | `include/libcamera/internal/value_node.h:264` | – | 확인 필요 |
| `libcamera::ValueNode::Adapter` | `include/libcamera/internal/value_node.h:82` | – | 확인 필요 |
| `libcamera::ValueNode::ConstDictAdapter` | `include/libcamera/internal/value_node.h:161` | `libcamera::ValueNode::Adapter` | 확인 필요 |
| `libcamera::ValueNode::ConstListAdapter` | `include/libcamera/internal/value_node.h:169` | `libcamera::ValueNode::Adapter` | 확인 필요 |
| `libcamera::ValueNode::DictAdapter` | `include/libcamera/internal/value_node.h:147` | `libcamera::ValueNode::Adapter` | 확인 필요 |
| `libcamera::ValueNode::DictIterator` | `include/libcamera/internal/value_node.h:129` | `libcamera::ValueNode::Iterator` | 확인 필요 |
| `libcamera::ValueNode::Iterator` | `include/libcamera/internal/value_node.h:43` | – | 확인 필요 |
| `libcamera::ValueNode::ListAdapter` | `include/libcamera/internal/value_node.h:155` | `libcamera::ValueNode::Adapter` | 확인 필요 |
| `libcamera::ValueNode::ListIterator` | `include/libcamera/internal/value_node.h:105` | `libcamera::ValueNode::Iterator` | 확인 필요 |
| `libcamera::ValueNode::Type` | `include/libcamera/internal/value_node.h:256` | – | 확인 필요 |
| `libcamera::ValueNode::Value` | `include/libcamera/internal/value_node.h:29` | – | 확인 필요 |
| `libcamera::Vector` | `include/libcamera/internal/vector.h:34` | – | Vector class |
| `libcamera::YamlParser` | `include/libcamera/internal/yaml_parser.h:18` | – | A helper class for parsing a YAML file |
| `libcamera::eGL` | `include/libcamera/internal/egl.h:102` | – | Helper class for managing OpenGL ES operations |
| `libcamera::eGL::VTable` | `include/libcamera/internal/egl.h:152` | – | 확인 필요 |
| `libcamera::eGLImage` | `include/libcamera/internal/egl.h:52` | – | Helper class for managing EGL image resources |
| `std::hash` | `include/libcamera/internal/v4l2_pixelformat.h:65` | – | 확인 필요 |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::appendPOD` | – | `include/libcamera/internal/ipa_data_serializer.h:35` | 확인 필요 |
| `libcamera::logCategoryIPADataSerializer` | `include/libcamera/internal/ipa_data_serializer.h:29` | – | 확인 필요 |
| `libcamera::logCategoryIPAManager` | `include/libcamera/internal/ipa_manager.h:23` | – | 확인 필요 |
| `libcamera::logCategoryMatrix` | `include/libcamera/internal/matrix.h:21` | – | 확인 필요 |
| `libcamera::logCategorySoftwareIsp` | `include/libcamera/internal/software_isp/software_isp.h:45` | – | 확인 필요 |
| `libcamera::logCategoryVector` | `include/libcamera/internal/vector.h:26` | – | 확인 필요 |
| `libcamera::logCategoryeGL` | `include/libcamera/internal/egl.h:37` | – | 확인 필요 |
| `libcamera::matrixInvert` | `include/libcamera/internal/matrix.h:25` | `src/libcamera/matrix.cpp:185` | 확인 필요 |
| `libcamera::matrixValidateValueNode` | `include/libcamera/internal/matrix.h:210` | `src/libcamera/matrix.cpp:335` | The value node shall be a list of numerical values. Its size shall be equal to the product of the number of rows and columns of the matrix (Rows x Cols). The values shall be stored in row-major order. |
| `libcamera::operator+` | – | `include/libcamera/internal/matrix.h:197` | 확인 필요 |
| `libcamera::readPOD` | – | `include/libcamera/internal/ipa_data_serializer.h:44` | 확인 필요 |
| `libcamera::sysfs::charDevPath` | `include/libcamera/internal/sysfs.h:16` | `src/libcamera/sysfs.cpp:34` | Retrieve the sysfs path for a character device |
| `libcamera::sysfs::firmwareNodePath` | `include/libcamera/internal/sysfs.h:18` | `src/libcamera/sysfs.cpp:70` | Retrieve the path of the firmware node for a device |
| `libcamera::vectorValidateValueNode` | `include/libcamera/internal/vector.h:353` | `src/libcamera/vector.cpp:362` | 확인 필요 |

## include/libcamera/ipa

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::IPAInterface` | `include/libcamera/ipa/ipa_interface.h:17` | – | Structs and enums that are defined in core.mojom that have the skipHeader tag must be #included here. |
| `libcamera::IPAModuleInfo` | `include/libcamera/ipa/ipa_module_info.h:16` | – | Information of an IPA module |
| `libcamera::ipa_control_info_entry` | `include/libcamera/ipa/ipa_controls.h:49` | – | Description of a serialized ControlInfo entry |
| `libcamera::ipa_control_list_entry` | `include/libcamera/ipa/ipa_controls.h:44` | – | Description of a serialized ControlList entry |
| `libcamera::ipa_control_value_entry` | `include/libcamera/ipa/ipa_controls.h:36` | – | Description of a serialized ControlValue entry |
| `libcamera::ipa_controls_header` | `include/libcamera/ipa/ipa_controls.h:26` | – | Serialized control packet header |
| `libcamera::ipa_controls_id_map_type` | `include/libcamera/ipa/ipa_controls.h:20` | – | 확인 필요 |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::ipaCreate` | `include/libcamera/ipa/ipa_interface.h:24` | `src/ipa/ipu3/ipu3.cpp:590` | Create an instance of the IPA interface |

## src/apps/cam

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `(unnamed enum at src/apps/cam/main.h:10:1)` | `src/apps/cam/main.h:10` | – | 확인 필요 |
| `CamApp` | `src/apps/cam/main.cpp:30` | – | 확인 필요 |
| `CameraSession` | `src/apps/cam/camera_session.h:29` | – | 확인 필요 |
| `CaptureScript` | `src/apps/cam/capture_script.h:19` | – | 확인 필요 |
| `CaptureScript::EventDeleter` | `src/apps/cam/capture_script.h:30` | – | 확인 필요 |
| `DRM::AtomicRequest` | `src/apps/cam/drm.h:248` | – | 확인 필요 |
| `DRM::AtomicRequest::Flags` | `src/apps/cam/drm.h:251` | – | 확인 필요 |
| `DRM::Blob` | `src/apps/cam/drm.h:129` | `DRM::Object` | 확인 필요 |
| `DRM::Connector` | `src/apps/cam/drm.h:175` | `DRM::Object` | 확인 필요 |
| `DRM::Connector::Status` | `src/apps/cam/drm.h:178` | – | 확인 필요 |
| `DRM::Crtc` | `src/apps/cam/drm.h:146` | `DRM::Object` | 확인 필요 |
| `DRM::Device` | `src/apps/cam/drm.h:283` | – | 확인 필요 |
| `DRM::Encoder` | `src/apps/cam/drm.h:161` | `DRM::Object` | 확인 필요 |
| `DRM::FrameBuffer` | `src/apps/cam/drm.h:231` | `DRM::Object` | 확인 필요 |
| `DRM::FrameBuffer::Plane` | `src/apps/cam/drm.h:234` | – | 확인 필요 |
| `DRM::Mode` | `src/apps/cam/drm.h:138` | – | 확인 필요 |
| `DRM::Object` | `src/apps/cam/drm.h:38` | – | 확인 필요 |
| `DRM::Object::Type` | `src/apps/cam/drm.h:41` | – | 확인 필요 |
| `DRM::Plane` | `src/apps/cam/drm.h:202` | `DRM::Object` | 확인 필요 |
| `DRM::Plane::Type` | `src/apps/cam/drm.h:205` | – | 확인 필요 |
| `DRM::Property` | `src/apps/cam/drm.h:80` | `DRM::Object` | 확인 필요 |
| `DRM::Property::Type` | `src/apps/cam/drm.h:83` | – | 확인 필요 |
| `DRM::PropertyValue` | `src/apps/cam/drm.h:113` | – | 확인 필요 |
| `FileSink` | `src/apps/cam/file_sink.h:21` | `FrameSink` | 확인 필요 |
| `FileSink::FileType` | `src/apps/cam/file_sink.h:39` | – | 확인 필요 |
| `FrameSink` | `src/apps/cam/frame_sink.h:18` | – | Abstract class to model a consumer of frames |
| `KMSSink` | `src/apps/cam/kms_sink.h:25` | `FrameSink` | 확인 필요 |
| `KMSSink::Request` | `src/apps/cam/kms_sink.h:39` | – | 확인 필요 |

## src/apps/common

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `EventLoop` | `src/apps/common/event_loop.h:23` | – | 확인 필요 |
| `EventLoop::Event` | `src/apps/common/event_loop.h:50` | – | 확인 필요 |
| `EventLoop::EventType` | `src/apps/common/event_loop.h:26` | – | 확인 필요 |
| `Image` | `src/apps/common/image.h:20` | – | 확인 필요 |
| `Image::MapMode` | `src/apps/common/image.h:23` | – | 확인 필요 |
| `KeyValueParser` | `src/apps/common/options.h:56` | – | A specialized parser for list of key-value pairs |
| `KeyValueParser::Options` | `src/apps/common/options.h:59` | `OptionsBase` | An option list generated by the key-value parser |
| `Option` | `src/apps/common/options.cpp:97` | – | Store metadata about an option |
| `OptionArgument` | `src/apps/common/options.h:20` | – | 확인 필요 |
| `OptionType` | `src/apps/common/options.h:26` | – | 확인 필요 |
| `OptionValue` | `src/apps/common/options.h:118` | – | Container to store the value of an option |
| `OptionValue::ValueType` | `src/apps/common/options.h:121` | – | 확인 필요 |
| `OptionsBase` | `src/apps/common/options.h:34` | – | 확인 필요 |
| `OptionsParser` | `src/apps/common/options.h:82` | – | A command line options parser |
| `OptionsParser::Options` | `src/apps/common/options.h:85` | `OptionsBase` | An option list generated by the options parser |
| `PPMWriter` | `src/apps/common/ppm_writer.h:14` | – | 확인 필요 |
| `StreamKeyValueParser` | `src/apps/common/stream_options.h:16` | `KeyValueParser` | 확인 필요 |

## src/apps/ipa-verify

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `isSignatureValid` | – | `src/apps/ipa-verify/main.cpp:21` | 확인 필요 |

## src/apps/lc-compliance

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `(unnamed enum at src/apps/lc-compliance/main.cpp:23:1)` | `src/apps/lc-compliance/main.cpp:23` | – | 확인 필요 |
| `CameraHolder` | `src/apps/lc-compliance/test_base.h:13` | – | 확인 필요 |
| `Capture` | `src/apps/lc-compliance/helpers/capture.h:18` | – | 확인 필요 |
| `Environment` | `src/apps/lc-compliance/environment.h:12` | – | 확인 필요 |
| `SimpleCapture` | `src/apps/lc-compliance/tests/capture_test.cpp:24` | `CameraHolder` | 확인 필요 |
| `SimpleCapture_CaptureStartStop_Test` | `src/apps/lc-compliance/tests/capture_test.cpp:86` | `SimpleCapture` | Test multiple start/stop cycles |
| `SimpleCapture_Capture_Test` | `src/apps/lc-compliance/tests/capture_test.cpp:68` | `SimpleCapture` | Test single capture cycles |
| `SimpleCapture_UnbalancedStop_Test` | `src/apps/lc-compliance/tests/capture_test.cpp:106` | `SimpleCapture` | Test unbalanced stop |
| `ThrowListener` | `src/apps/lc-compliance/main.cpp:35` | – | Make asserts act like exceptions, otherwise they only fail (or skip) the current function. From gtest documentation: https://google.github.io/googletest/advanced.html#asserting-on-subroutines-with-an- |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `gtest_MultiStreamSimpleCapture_EvalGenerateName_` | – | `src/apps/lc-compliance/tests/capture_test.cpp:139` | 확인 필요 |
| `gtest_MultiStreamSimpleCapture_EvalGenerator_` | – | `src/apps/lc-compliance/tests/capture_test.cpp:139` | 확인 필요 |
| `gtest_SingleStreamSimpleCapture_EvalGenerateName_` | – | `src/apps/lc-compliance/tests/capture_test.cpp:133` | 확인 필요 |
| `gtest_SingleStreamSimpleCapture_EvalGenerator_` | – | `src/apps/lc-compliance/tests/capture_test.cpp:133` | 확인 필요 |
| `initCamera` | – | `src/apps/lc-compliance/main.cpp:51` | 확인 필요 |
| `initGtest` | – | `src/apps/lc-compliance/main.cpp:108` | 확인 필요 |
| `initGtestParameters` | – | `src/apps/lc-compliance/main.cpp:81` | 확인 필요 |
| `listCameras` | – | `src/apps/lc-compliance/main.cpp:45` | 확인 필요 |
| `parseOptions` | – | `src/apps/lc-compliance/main.cpp:119` | 확인 필요 |

## src/gstreamer

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `(unnamed enum at src/gstreamer/gstlibcamerapad.cpp:26:1)` | `src/gstreamer/gstlibcamerapad.cpp:26` | – | 확인 필요 |
| `(unnamed enum at src/gstreamer/gstlibcamerapool.cpp:19:1)` | `src/gstreamer/gstlibcamerapool.cpp:19` | – | 확인 필요 |
| `(unnamed enum at src/gstreamer/gstlibcameraprovider.cpp:35:1)` | `src/gstreamer/gstlibcameraprovider.cpp:35` | – | libcamera GstDevice implementation |
| `(unnamed enum at src/gstreamer/gstlibcamerasrc.cpp:154:1)` | `src/gstreamer/gstlibcamerasrc.cpp:154` | – | 확인 필요 |
| `(unnamed struct at src/gstreamer/gstlibcamera-utils.cpp:18:14)` | `src/gstreamer/gstlibcamera-utils.cpp:18` | – | 확인 필요 |
| `(unnamed struct at src/gstreamer/gstlibcamera-utils.cpp:267:14)` | `src/gstreamer/gstlibcamera-utils.cpp:267` | – | 확인 필요 |
| `(unnamed struct at src/gstreamer/gstlibcamera-utils.cpp:336:14)` | `src/gstreamer/gstlibcamera-utils.cpp:336` | – | 확인 필요 |
| `FrameWrap` | `src/gstreamer/gstlibcameraallocator.cpp:33` | – | An internal wrapper to track the relation between FrameBuffer and GstMemory(s) |
| `GLibLocker` | `src/gstreamer/gstlibcamera-utils.h:57` | – | A simple scoped mutex locker for GMutex |
| `GLibRecLocker` | `src/gstreamer/gstlibcamera-utils.h:85` | – | A simple scoped mutex locker for GRecMutex |
| `GstLibcameraAllocatorClass` | `src/gstreamer/gstlibcameraallocator.h:18` | – | 확인 필요 |
| `GstLibcameraDeviceClass` | `src/gstreamer/gstlibcameraprovider.cpp:40` | – | 확인 필요 |
| `GstLibcameraPadClass` | `src/gstreamer/gstlibcamerapad.h:18` | – | 확인 필요 |
| `GstLibcameraPoolClass` | `src/gstreamer/gstlibcamerapool.h:22` | – | 확인 필요 |
| `GstLibcameraProviderClass` | `src/gstreamer/gstlibcameraprovider.h:16` | – | 확인 필요 |
| `GstLibcameraSrcClass` | `src/gstreamer/gstlibcamerasrc.h:16` | – | 확인 필요 |
| `GstLibcameraSrcState` | `src/gstreamer/gstlibcamerasrc.cpp:105` | – | Used for C++ object with destructors. |
| `RequestWrap` | `src/gstreamer/gstlibcamerasrc.cpp:47` | – | 확인 필요 |
| `_GstLibcameraAllocator` | `src/gstreamer/gstlibcameraallocator.cpp:97` | – | A pooling GstDmaBufAllocator for libcamera |
| `_GstLibcameraDevice` | `src/gstreamer/gstlibcameraprovider.cpp:43` | – | libcamera GstDevice implementation |
| `_GstLibcameraPad` | `src/gstreamer/gstlibcamerapad.cpp:17` | – | 확인 필요 |
| `_GstLibcameraPool` | `src/gstreamer/gstlibcamerapool.cpp:26` | – | 확인 필요 |
| `_GstLibcameraProvider` | `src/gstreamer/gstlibcameraprovider.cpp:177` | – | libcamera GstDeviceProvider implementation |
| `_GstLibcameraSrc` | `src/gstreamer/gstlibcamerasrc.cpp:138` | – | 확인 필요 |
| `libcamera::GstCameraControls` | `src/gstreamer/gstlibcamera-controls.h:21` | – | 확인 필요 |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `GST_LIBCAMERA_ALLOCATOR` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `GST_LIBCAMERA_DEVICE` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `GST_LIBCAMERA_IS_ALLOCATOR` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `GST_LIBCAMERA_IS_DEVICE` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `GST_LIBCAMERA_IS_PAD` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `GST_LIBCAMERA_IS_POOL` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `GST_LIBCAMERA_IS_PROVIDER` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `GST_LIBCAMERA_IS_SRC` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `GST_LIBCAMERA_PAD` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `GST_LIBCAMERA_POOL` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `GST_LIBCAMERA_PROVIDER` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `GST_LIBCAMERA_SRC` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `bare_structure_from_format` | – | `src/gstreamer/gstlibcamera-utils.cpp:314` | 확인 필요 |
| `bayer_format_from_string` | – | `src/gstreamer/gstlibcamera-utils.cpp:304` | 확인 필요 |
| `bayer_format_to_string` | – | `src/gstreamer/gstlibcamera-utils.cpp:294` | 확인 필요 |
| `colorimetry_from_colorspace` | – | `src/gstreamer/gstlibcamera-utils.cpp:94` | 확인 필요 |
| `colorspace_from_colorimetry` | – | `src/gstreamer/gstlibcamera-utils.cpp:155` | 확인 필요 |
| `control_type_to_gtype` | – | `src/gstreamer/gstlibcamera-utils.cpp:354` | 확인 필요 |
| `glib_autoptr_cleanup_GstLibcameraAllocator` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `glib_autoptr_cleanup_GstLibcameraAllocatorClass` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `glib_autoptr_cleanup_GstLibcameraDevice` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `glib_autoptr_cleanup_GstLibcameraDeviceClass` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `glib_autoptr_cleanup_GstLibcameraPad` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `glib_autoptr_cleanup_GstLibcameraPadClass` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `glib_autoptr_cleanup_GstLibcameraPool` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `glib_autoptr_cleanup_GstLibcameraPoolClass` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `glib_autoptr_cleanup_GstLibcameraProvider` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `glib_autoptr_cleanup_GstLibcameraProviderClass` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `glib_autoptr_cleanup_GstLibcameraSrc` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `glib_autoptr_cleanup_GstLibcameraSrcClass` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `glib_autoptr_clear_GstLibcameraAllocator` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `glib_autoptr_clear_GstLibcameraAllocatorClass` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `glib_autoptr_clear_GstLibcameraDevice` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `glib_autoptr_clear_GstLibcameraDeviceClass` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `glib_autoptr_clear_GstLibcameraPad` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `glib_autoptr_clear_GstLibcameraPadClass` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `glib_autoptr_clear_GstLibcameraPool` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `glib_autoptr_clear_GstLibcameraPoolClass` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `glib_autoptr_clear_GstLibcameraProvider` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `glib_autoptr_clear_GstLibcameraProviderClass` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `glib_autoptr_clear_GstLibcameraSrc` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `glib_autoptr_clear_GstLibcameraSrcClass` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `glib_autoptr_destroy_GstLibcameraAllocator` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `glib_autoptr_destroy_GstLibcameraAllocatorClass` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `glib_autoptr_destroy_GstLibcameraDevice` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `glib_autoptr_destroy_GstLibcameraDeviceClass` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `glib_autoptr_destroy_GstLibcameraPad` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `glib_autoptr_destroy_GstLibcameraPadClass` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `glib_autoptr_destroy_GstLibcameraPool` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `glib_autoptr_destroy_GstLibcameraPoolClass` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `glib_autoptr_destroy_GstLibcameraProvider` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `glib_autoptr_destroy_GstLibcameraProviderClass` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `glib_autoptr_destroy_GstLibcameraSrc` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `glib_autoptr_destroy_GstLibcameraSrcClass` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `glib_listautoptr_cleanup_GstLibcameraAllocator` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `glib_listautoptr_cleanup_GstLibcameraAllocatorClass` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `glib_listautoptr_cleanup_GstLibcameraDevice` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `glib_listautoptr_cleanup_GstLibcameraDeviceClass` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `glib_listautoptr_cleanup_GstLibcameraPad` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `glib_listautoptr_cleanup_GstLibcameraPadClass` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `glib_listautoptr_cleanup_GstLibcameraPool` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `glib_listautoptr_cleanup_GstLibcameraPoolClass` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `glib_listautoptr_cleanup_GstLibcameraProvider` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `glib_listautoptr_cleanup_GstLibcameraProviderClass` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `glib_listautoptr_cleanup_GstLibcameraSrc` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `glib_listautoptr_cleanup_GstLibcameraSrcClass` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `glib_queueautoptr_cleanup_GstLibcameraAllocator` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `glib_queueautoptr_cleanup_GstLibcameraAllocatorClass` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `glib_queueautoptr_cleanup_GstLibcameraDevice` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `glib_queueautoptr_cleanup_GstLibcameraDeviceClass` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `glib_queueautoptr_cleanup_GstLibcameraPad` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `glib_queueautoptr_cleanup_GstLibcameraPadClass` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `glib_queueautoptr_cleanup_GstLibcameraPool` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `glib_queueautoptr_cleanup_GstLibcameraPoolClass` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `glib_queueautoptr_cleanup_GstLibcameraProvider` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `glib_queueautoptr_cleanup_GstLibcameraProviderClass` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `glib_queueautoptr_cleanup_GstLibcameraSrc` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `glib_queueautoptr_cleanup_GstLibcameraSrcClass` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `glib_slistautoptr_cleanup_GstLibcameraAllocator` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `glib_slistautoptr_cleanup_GstLibcameraAllocatorClass` | – | `src/gstreamer/gstlibcameraallocator.h:18` | 확인 필요 |
| `glib_slistautoptr_cleanup_GstLibcameraDevice` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `glib_slistautoptr_cleanup_GstLibcameraDeviceClass` | – | `src/gstreamer/gstlibcameraprovider.cpp:40` | 확인 필요 |
| `glib_slistautoptr_cleanup_GstLibcameraPad` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `glib_slistautoptr_cleanup_GstLibcameraPadClass` | – | `src/gstreamer/gstlibcamerapad.h:18` | 확인 필요 |
| `glib_slistautoptr_cleanup_GstLibcameraPool` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `glib_slistautoptr_cleanup_GstLibcameraPoolClass` | – | `src/gstreamer/gstlibcamerapool.h:22` | 확인 필요 |
| `glib_slistautoptr_cleanup_GstLibcameraProvider` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `glib_slistautoptr_cleanup_GstLibcameraProviderClass` | – | `src/gstreamer/gstlibcameraprovider.h:16` | 확인 필요 |
| `glib_slistautoptr_cleanup_GstLibcameraSrc` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `glib_slistautoptr_cleanup_GstLibcameraSrcClass` | – | `src/gstreamer/gstlibcamerasrc.h:16` | 확인 필요 |
| `gst_format_to_pixel_format` | – | `src/gstreamer/gstlibcamera-utils.cpp:256` | 확인 필요 |
| `gst_libcamera_allocator_class_init` | `src/gstreamer/gstlibcameraallocator.cpp:112` | `src/gstreamer/gstlibcameraallocator.cpp:190` | 확인 필요 |
| `gst_libcamera_allocator_class_intern_init` | – | `src/gstreamer/gstlibcameraallocator.cpp:112` | 확인 필요 |
| `gst_libcamera_allocator_dispose` | – | `src/gstreamer/gstlibcameraallocator.cpp:164` | 확인 필요 |
| `gst_libcamera_allocator_finalize` | – | `src/gstreamer/gstlibcameraallocator.cpp:177` | 확인 필요 |
| `gst_libcamera_allocator_free_pool` | – | `src/gstreamer/gstlibcameraallocator.cpp:142` | 확인 필요 |
| `gst_libcamera_allocator_get_instance_private` | – | `src/gstreamer/gstlibcameraallocator.cpp:112` | 확인 필요 |
| `gst_libcamera_allocator_get_pool_size` | `src/gstreamer/gstlibcameraallocator.h:28` | `src/gstreamer/gstlibcameraallocator.cpp:257` | 확인 필요 |
| `gst_libcamera_allocator_get_type` | `src/gstreamer/gstlibcameraallocator.h:18` | `src/gstreamer/gstlibcameraallocator.cpp:112` | 확인 필요 |
| `gst_libcamera_allocator_get_type_once` | `src/gstreamer/gstlibcameraallocator.cpp:112` | – | 확인 필요 |
| `gst_libcamera_allocator_init` | `src/gstreamer/gstlibcameraallocator.cpp:112` | `src/gstreamer/gstlibcameraallocator.cpp:156` | 확인 필요 |
| `gst_libcamera_allocator_new` | `src/gstreamer/gstlibcameraallocator.h:21` | `src/gstreamer/gstlibcameraallocator.cpp:201` | 확인 필요 |
| `gst_libcamera_allocator_prepare_buffer` | `src/gstreamer/gstlibcameraallocator.h:24` | `src/gstreamer/gstlibcameraallocator.cpp:235` | 확인 필요 |
| `gst_libcamera_allocator_release` | `src/gstreamer/gstlibcameraallocator.cpp:21` | `src/gstreamer/gstlibcameraallocator.cpp:116` | 확인 필요 |
| `gst_libcamera_buffer_add_video_meta` | – | `src/gstreamer/gstlibcamerapool.cpp:138` | 확인 필요 |
| `gst_libcamera_buffer_get_frame_buffer` | `src/gstreamer/gstlibcamerapool.h:29` | `src/gstreamer/gstlibcamerapool.cpp:174` | 확인 필요 |
| `gst_libcamera_clamp_and_set_frameduration` | `src/gstreamer/gstlibcamera-utils.h:24` | `src/gstreamer/gstlibcamera-utils.cpp:556` | 확인 필요 |
| `gst_libcamera_configure_stream_from_caps` | `src/gstreamer/gstlibcamera-utils.h:21` | `src/gstreamer/gstlibcamera-utils.cpp:441` | 확인 필요 |
| `gst_libcamera_create_video_pool` | – | `src/gstreamer/gstlibcamerasrc.cpp:538` | Create a video pool for a pad |
| `gst_libcamera_device_class_init` | `src/gstreamer/gstlibcameraprovider.cpp:48` | `src/gstreamer/gstlibcameraprovider.cpp:111` | 확인 필요 |
| `gst_libcamera_device_class_intern_init` | – | `src/gstreamer/gstlibcameraprovider.cpp:48` | 확인 필요 |
| `gst_libcamera_device_create_element` | – | `src/gstreamer/gstlibcameraprovider.cpp:51` | 확인 필요 |
| `gst_libcamera_device_finalize` | – | `src/gstreamer/gstlibcameraprovider.cpp:100` | 확인 필요 |
| `gst_libcamera_device_get_instance_private` | – | `src/gstreamer/gstlibcameraprovider.cpp:48` | 확인 필요 |
| `gst_libcamera_device_get_type` | `src/gstreamer/gstlibcameraprovider.cpp:40` | `src/gstreamer/gstlibcameraprovider.cpp:48` | 확인 필요 |
| `gst_libcamera_device_get_type_once` | `src/gstreamer/gstlibcameraprovider.cpp:48` | – | 확인 필요 |
| `gst_libcamera_device_init` | `src/gstreamer/gstlibcameraprovider.cpp:48` | `src/gstreamer/gstlibcameraprovider.cpp:95` | 확인 필요 |
| `gst_libcamera_device_new` | – | `src/gstreamer/gstlibcameraprovider.cpp:130` | 확인 필요 |
| `gst_libcamera_device_reconfigure_element` | – | `src/gstreamer/gstlibcameraprovider.cpp:67` | 확인 필요 |
| `gst_libcamera_device_set_property` | – | `src/gstreamer/gstlibcameraprovider.cpp:79` | 확인 필요 |
| `gst_libcamera_extrapolate_info` | – | `src/gstreamer/gstlibcamerasrc.cpp:271` | 확인 필요 |
| `gst_libcamera_framerate_to_caps` | `src/gstreamer/gstlibcamera-utils.h:27` | `src/gstreamer/gstlibcamera-utils.cpp:599` | 확인 필요 |
| `gst_libcamera_get_camera_manager` | `src/gstreamer/gstlibcamera-utils.h:51` | `src/gstreamer/gstlibcamera-utils.cpp:717` | 확인 필요 |
| `gst_libcamera_get_framerate_from_caps` | `src/gstreamer/gstlibcamera-utils.h:23` | `src/gstreamer/gstlibcamera-utils.cpp:537` | 확인 필요 |
| `gst_libcamera_gvalue_get_rectangle` | `src/gstreamer/gstlibcamera-utils.h:31` | `src/gstreamer/gstlibcamera-utils.cpp:646` | 확인 필요 |
| `gst_libcamera_gvalue_set_point` | `src/gstreamer/gstlibcamera-utils.h:28` | `src/gstreamer/gstlibcamera-utils.cpp:614` | 확인 필요 |
| `gst_libcamera_gvalue_set_rectangle` | `src/gstreamer/gstlibcamera-utils.h:30` | `src/gstreamer/gstlibcamera-utils.cpp:640` | 확인 필요 |
| `gst_libcamera_gvalue_set_size` | `src/gstreamer/gstlibcamera-utils.h:29` | `src/gstreamer/gstlibcamera-utils.cpp:627` | 확인 필요 |
| `gst_libcamera_memory_get_frame_buffer` | `src/gstreamer/gstlibcameraallocator.h:31` | `src/gstreamer/gstlibcameraallocator.cpp:269` | 확인 필요 |
| `gst_libcamera_pad_class_init` | `src/gstreamer/gstlibcamerapad.cpp:31` | `src/gstreamer/gstlibcamerapad.cpp:124` | 확인 필요 |
| `gst_libcamera_pad_class_intern_init` | – | `src/gstreamer/gstlibcamerapad.cpp:31` | 확인 필요 |
| `gst_libcamera_pad_get_instance_private` | – | `src/gstreamer/gstlibcamerapad.cpp:31` | 확인 필요 |
| `gst_libcamera_pad_get_pool` | `src/gstreamer/gstlibcamerapad.h:22` | `src/gstreamer/gstlibcamerapad.cpp:151` | 확인 필요 |
| `gst_libcamera_pad_get_property` | – | `src/gstreamer/gstlibcamerapad.cpp:51` | 확인 필요 |
| `gst_libcamera_pad_get_role` | `src/gstreamer/gstlibcamerapad.h:20` | `src/gstreamer/gstlibcamerapad.cpp:143` | 확인 필요 |
| `gst_libcamera_pad_get_stream` | `src/gstreamer/gstlibcamerapad.h:34` | `src/gstreamer/gstlibcamerapad.cpp:197` | 확인 필요 |
| `gst_libcamera_pad_get_type` | `src/gstreamer/gstlibcamerapad.h:18` | `src/gstreamer/gstlibcamerapad.cpp:31` | 확인 필요 |
| `gst_libcamera_pad_get_type_once` | `src/gstreamer/gstlibcamerapad.cpp:31` | – | 확인 필요 |
| `gst_libcamera_pad_get_video_info` | `src/gstreamer/gstlibcamerapad.h:30` | `src/gstreamer/gstlibcamerapad.cpp:183` | 확인 필요 |
| `gst_libcamera_pad_get_video_pool` | `src/gstreamer/gstlibcamerapad.h:26` | `src/gstreamer/gstlibcamerapad.cpp:168` | 확인 필요 |
| `gst_libcamera_pad_init` | `src/gstreamer/gstlibcamerapad.cpp:31` | `src/gstreamer/gstlibcamerapad.cpp:86` | 확인 필요 |
| `gst_libcamera_pad_query` | – | `src/gstreamer/gstlibcamerapad.cpp:68` | 확인 필요 |
| `gst_libcamera_pad_set_latency` | `src/gstreamer/gstlibcamerapad.h:38` | `src/gstreamer/gstlibcamerapad.cpp:209` | 확인 필요 |
| `gst_libcamera_pad_set_pool` | `src/gstreamer/gstlibcamerapad.h:24` | `src/gstreamer/gstlibcamerapad.cpp:158` | 확인 필요 |
| `gst_libcamera_pad_set_property` | – | `src/gstreamer/gstlibcamerapad.cpp:34` | 확인 필요 |
| `gst_libcamera_pad_set_stream` | `src/gstreamer/gstlibcamerapad.h:36` | `src/gstreamer/gstlibcamerapad.cpp:203` | 확인 필요 |
| `gst_libcamera_pad_set_video_info` | `src/gstreamer/gstlibcamerapad.h:32` | `src/gstreamer/gstlibcamerapad.cpp:189` | 확인 필요 |
| `gst_libcamera_pad_set_video_pool` | `src/gstreamer/gstlibcamerapad.h:28` | `src/gstreamer/gstlibcamerapad.cpp:174` | 확인 필요 |
| `gst_libcamera_pool_acquire_buffer` | – | `src/gstreamer/gstlibcamerapool.cpp:52` | 확인 필요 |
| `gst_libcamera_pool_class_init` | `src/gstreamer/gstlibcamerapool.cpp:34` | `src/gstreamer/gstlibcamerapool.cpp:120` | 확인 필요 |
| `gst_libcamera_pool_class_intern_init` | – | `src/gstreamer/gstlibcamerapool.cpp:34` | 확인 필요 |
| `gst_libcamera_pool_finalize` | – | `src/gstreamer/gstlibcamerapool.cpp:105` | 확인 필요 |
| `gst_libcamera_pool_get_instance_private` | – | `src/gstreamer/gstlibcamerapool.cpp:34` | 확인 필요 |
| `gst_libcamera_pool_get_stream` | `src/gstreamer/gstlibcamerapool.h:27` | `src/gstreamer/gstlibcamerapool.cpp:168` | 확인 필요 |
| `gst_libcamera_pool_get_type` | `src/gstreamer/gstlibcamerapool.h:22` | `src/gstreamer/gstlibcamerapool.cpp:34` | 확인 필요 |
| `gst_libcamera_pool_get_type_once` | `src/gstreamer/gstlibcamerapool.cpp:34` | – | 확인 필요 |
| `gst_libcamera_pool_init` | `src/gstreamer/gstlibcamerapool.cpp:34` | `src/gstreamer/gstlibcamerapool.cpp:99` | 확인 필요 |
| `gst_libcamera_pool_new` | `src/gstreamer/gstlibcamerapool.h:24` | `src/gstreamer/gstlibcamerapool.cpp:149` | 확인 필요 |
| `gst_libcamera_pool_pop_buffer` | – | `src/gstreamer/gstlibcamerapool.cpp:37` | 확인 필요 |
| `gst_libcamera_pool_release_buffer` | – | `src/gstreamer/gstlibcamerapool.cpp:83` | 확인 필요 |
| `gst_libcamera_pool_reset_buffer` | – | `src/gstreamer/gstlibcamerapool.cpp:72` | 확인 필요 |
| `gst_libcamera_provider_class_init` | `src/gstreamer/gstlibcameraprovider.cpp:181` | `src/gstreamer/gstlibcameraprovider.cpp:235` | 확인 필요 |
| `gst_libcamera_provider_class_intern_init` | – | `src/gstreamer/gstlibcameraprovider.cpp:181` | 확인 필요 |
| `gst_libcamera_provider_get_instance_private` | – | `src/gstreamer/gstlibcameraprovider.cpp:181` | 확인 필요 |
| `gst_libcamera_provider_get_type` | `src/gstreamer/gstlibcameraprovider.h:16` | `src/gstreamer/gstlibcameraprovider.cpp:181` | 확인 필요 |
| `gst_libcamera_provider_get_type_once` | `src/gstreamer/gstlibcameraprovider.cpp:181` | – | 확인 필요 |
| `gst_libcamera_provider_init` | `src/gstreamer/gstlibcameraprovider.cpp:181` | `src/gstreamer/gstlibcameraprovider.cpp:226` | 확인 필요 |
| `gst_libcamera_provider_probe` | – | `src/gstreamer/gstlibcameraprovider.cpp:187` | 확인 필요 |
| `gst_libcamera_set_structure_field` | `src/gstreamer/gstlibcamera-utils.h:32` | `src/gstreamer/gstlibcamera-utils.cpp:737` | 확인 필요 |
| `gst_libcamera_src_change_state` | – | `src/gstreamer/gstlibcamerasrc.cpp:1035` | 확인 필요 |
| `gst_libcamera_src_child_proxy_get_child_by_index` | – | `src/gstreamer/gstlibcamerasrc.cpp:1256` | GstChildProxy implementation |
| `gst_libcamera_src_child_proxy_get_children_count` | – | `src/gstreamer/gstlibcamerasrc.cpp:1270` | 확인 필요 |
| `gst_libcamera_src_child_proxy_init` | `src/gstreamer/gstlibcamerasrc.cpp:161` | `src/gstreamer/gstlibcamerasrc.cpp:1277` | 확인 필요 |
| `gst_libcamera_src_class_init` | `src/gstreamer/gstlibcamerasrc.cpp:164` | `src/gstreamer/gstlibcamerasrc.cpp:1204` | 확인 필요 |
| `gst_libcamera_src_class_intern_init` | – | `src/gstreamer/gstlibcamerasrc.cpp:164` | 확인 필요 |
| `gst_libcamera_src_close` | – | `src/gstreamer/gstlibcamerasrc.cpp:968` | 확인 필요 |
| `gst_libcamera_src_finalize` | – | `src/gstreamer/gstlibcamerasrc.cpp:1105` | 확인 필요 |
| `gst_libcamera_src_get_instance_private` | – | `src/gstreamer/gstlibcamerasrc.cpp:164` | 확인 필요 |
| `gst_libcamera_src_get_property` | – | `src/gstreamer/gstlibcamerasrc.cpp:1013` | 확인 필요 |
| `gst_libcamera_src_get_type` | `src/gstreamer/gstlibcamerasrc.h:16` | `src/gstreamer/gstlibcamerasrc.cpp:164` | 확인 필요 |
| `gst_libcamera_src_get_type_once` | `src/gstreamer/gstlibcamerasrc.cpp:164` | – | 확인 필요 |
| `gst_libcamera_src_init` | `src/gstreamer/gstlibcamerasrc.cpp:164` | `src/gstreamer/gstlibcamerasrc.cpp:1121` | 확인 필요 |
| `gst_libcamera_src_negotiate` | – | `src/gstreamer/gstlibcamerasrc.cpp:588` | Must be called with stream_lock held. |
| `gst_libcamera_src_open` | – | `src/gstreamer/gstlibcamerasrc.cpp:460` | 확인 필요 |
| `gst_libcamera_src_release_pad` | – | `src/gstreamer/gstlibcamerasrc.cpp:1174` | 확인 필요 |
| `gst_libcamera_src_request_new_pad` | – | `src/gstreamer/gstlibcamerasrc.cpp:1147` | 확인 필요 |
| `gst_libcamera_src_send_event` | – | `src/gstreamer/gstlibcamerasrc.cpp:1084` | 확인 필요 |
| `gst_libcamera_src_set_property` | – | `src/gstreamer/gstlibcamerasrc.cpp:989` | 확인 필요 |
| `gst_libcamera_src_task_enter` | – | `src/gstreamer/gstlibcamerasrc.cpp:829` | 확인 필요 |
| `gst_libcamera_src_task_leave` | – | `src/gstreamer/gstlibcamerasrc.cpp:941` | 확인 필요 |
| `gst_libcamera_src_task_run` | – | `src/gstreamer/gstlibcamerasrc.cpp:709` | 확인 필요 |
| `gst_libcamera_stream_configuration_to_caps` | `src/gstreamer/gstlibcamera-utils.h:19` | `src/gstreamer/gstlibcamera-utils.cpp:414` | 확인 필요 |
| `gst_libcamera_stream_formats_to_caps` | `src/gstreamer/gstlibcamera-utils.h:18` | `src/gstreamer/gstlibcamera-utils.cpp:364` | 확인 필요 |
| `gst_libcamera_stream_role_get_type` | – | `src/gstreamer/gstlibcamerapad.cpp:93` | 확인 필요 |
| `gst_libcamera_video_frame_copy` | – | `src/gstreamer/gstlibcamerasrc.cpp:287` | 확인 필요 |
| `gst_plugin_libcamera_get_desc` | `src/gstreamer/gstlibcamera.cpp:25` | – | 확인 필요 |
| `gst_plugin_libcamera_register` | `src/gstreamer/gstlibcamera.cpp:25` | – | 확인 필요 |
| `pixel_format_to_gst_format` | – | `src/gstreamer/gstlibcamera-utils.cpp:246` | 확인 필요 |
| `plugin_init` | – | `src/gstreamer/gstlibcamera.cpp:13` | 확인 필요 |

## src/ipa/ipu3

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::ipa::ipu3::IPAActiveState` | `src/ipa/ipu3/ipa_context.h:46` | – | The active state of the IPA algorithms |
| `libcamera::ipa::ipu3::IPAActiveState::(unnamed struct at src/ipa/ipu3/ipa_context.h:47:2)` | `src/ipa/ipu3/ipa_context.h:47` | – | 확인 필요 |
| `libcamera::ipa::ipu3::IPAContext` | `src/ipa/ipu3/ipa_context.h:73` | – | Global IPA context data shared between all algorithms |
| `libcamera::ipa::ipu3::IPAFrameContext` | `src/ipa/ipu3/ipa_context.h:60` | `libcamera::ipa::FrameContext` | IPU3-specific FrameContext |
| `libcamera::ipa::ipu3::IPAFrameContext::(unnamed struct at src/ipa/ipu3/ipa_context.h:61:2)` | `src/ipa/ipu3/ipa_context.h:61` | – | 확인 필요 |
| `libcamera::ipa::ipu3::IPAIPU3` | `src/ipa/ipu3/ipu3.cpp:139` | `libcamera::ipa::ipu3::IPAIPU3Interface`, `libcamera::ipa::ipu3::Module` | The IPU3 IPA implementation |
| `libcamera::ipa::ipu3::IPASessionConfiguration` | `src/ipa/ipu3/ipa_context.h:32` | – | Session configuration for the IPA module |
| `libcamera::ipa::ipu3::IPASessionConfiguration::(unnamed struct at src/ipa/ipu3/ipa_context.h:33:2)` | `src/ipa/ipu3/ipa_context.h:33` | – | 확인 필요 |
| `libcamera::ipa::ipu3::IPASessionConfiguration::(unnamed struct at src/ipa/ipu3/ipa_context.h:39:2)` | `src/ipa/ipu3/ipa_context.h:39` | – | 확인 필요 |
| `libcamera::ipa::ipu3::algorithms::Accumulator` | `src/ipa/ipu3/algorithms/awb.h:31` | – | RGB statistics for a given zone |
| `libcamera::ipa::ipu3::algorithms::Accumulator::(unnamed struct at src/ipa/ipu3/algorithms/awb.h:33:2)` | `src/ipa/ipu3/algorithms/awb.h:33` | – | 확인 필요 |
| `libcamera::ipa::ipu3::algorithms::Af` | `src/ipa/ipu3/algorithms/af.h:22` | `libcamera::ipa::ipu3::Algorithm` | An auto-focus algorithm based on IPU3 statistics |
| `libcamera::ipa::ipu3::algorithms::Af::y_table_item` | `src/ipa/ipu3/algorithms/af.h:25` | – | The format of y_table. From ipu3-ipa repo |
| `libcamera::ipa::ipu3::algorithms::Agc` | `src/ipa/ipu3/algorithms/agc.h:27` | `libcamera::ipa::ipu3::Algorithm` | A mean-based auto-exposure algorithm |
| `libcamera::ipa::ipu3::algorithms::AgcTraits` | `src/ipa/ipu3/algorithms/agc.cpp:152` | `libcamera::ipa::AgcMeanLuminance::Traits` | 확인 필요 |
| `libcamera::ipa::ipu3::algorithms::Awb` | `src/ipa/ipu3/algorithms/awb.h:40` | `libcamera::ipa::ipu3::Algorithm` | The IPU3 white balance correction algorithm implementation |
| `libcamera::ipa::ipu3::algorithms::BlackLevelCorrection` | `src/ipa/ipu3/algorithms/blc.h:16` | `libcamera::ipa::ipu3::Algorithm` | A class to handle black level correction |
| `libcamera::ipa::ipu3::algorithms::Ccm` | `src/ipa/ipu3/algorithms/ccm.h:26` | `libcamera::ipa::ipu3::Algorithm` | The IPU3 color correction matrix algorithm |
| `libcamera::ipa::ipu3::algorithms::Ipu3AwbStats` | `src/ipa/ipu3/algorithms/awb.cpp:34` | `libcamera::ipa::AwbStats` | The IPU3 specific implementation of AwbStats |
| `libcamera::ipa::ipu3::algorithms::Lsc` | `src/ipa/ipu3/algorithms/lsc.h:21` | `libcamera::ipa::ipu3::Algorithm` | IPU3 Lens Shading Correction algorithm |
| `libcamera::ipa::ipu3::algorithms::ToneMapping` | `src/ipa/ipu3/algorithms/tone_mapping.h:21` | `libcamera::ipa::ipu3::Algorithm` | A class to handle tone mapping based on gamma |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::ipa::ipu3::algorithms::logCategoryIPU3Af` | `src/ipa/ipu3/algorithms/af.cpp:60` | – | 확인 필요 |
| `libcamera::ipa::ipu3::algorithms::logCategoryIPU3Agc` | `src/ipa/ipu3/algorithms/agc.cpp:49` | – | A mean-based auto-exposure algorithm |
| `libcamera::ipa::ipu3::algorithms::logCategoryIPU3Awb` | `src/ipa/ipu3/algorithms/awb.cpp:24` | – | 확인 필요 |
| `libcamera::ipa::ipu3::algorithms::logCategoryIPU3Ccm` | `src/ipa/ipu3/algorithms/ccm.cpp:23` | – | The IPU3 color correction matrix algorithm |
| `libcamera::ipa::ipu3::algorithms::logCategoryIPU3Lsc` | `src/ipa/ipu3/algorithms/lsc.cpp:29` | – | IPU3 Lens Shading Correction algorithm |
| `libcamera::ipa::ipu3::algorithms::quantize` | – | `src/ipa/ipu3/algorithms/lsc.cpp:142` | 확인 필요 |
| `libcamera::logCategoryIPAIPU3` | `src/ipa/ipu3/ipu3.cpp:62` | – | 확인 필요 |

## src/ipa/libipa

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::LimitsRecorder` | `src/ipa/libipa/awb_bayes.cpp:64` | – | 확인 필요 |
| `libcamera::ipa::AgcAlgorithm` | `src/ipa/libipa/agc.h:121` | – | libIPA LSC algorithm algorithm |
| `libcamera::ipa::AgcAlgorithm::ConfigurationParams` | `src/ipa/libipa/agc.h:124` | – | Parameters for AgcAlgorithm::configure() |
| `libcamera::ipa::AgcAlgorithm::ProcessParams` | `src/ipa/libipa/agc.h:131` | – | Parameters for AgcAlgorithm::process() |
| `libcamera::ipa::AgcMSV` | `src/ipa/libipa/agc_msv.h:19` | – | Binned mean luminance based AGC algorithm |
| `libcamera::ipa::AgcMSV::Limits` | `src/ipa/libipa/agc_msv.h:22` | – | Set of limits for the algorithm |
| `libcamera::ipa::AgcMSV::Params` | `src/ipa/libipa/agc_msv.h:29` | – | Collection of parameters for the algorithm |
| `libcamera::ipa::AgcMSV::Result` | `src/ipa/libipa/agc_msv.h:35` | – | Collection of results of the algorithm |
| `libcamera::ipa::AgcMeanLuminance` | `src/ipa/libipa/agc_mean_luminance.h:26` | – | A mean-based auto-exposure algorithm |
| `libcamera::ipa::AgcMeanLuminance::AgcConstraint` | `src/ipa/libipa/agc_mean_luminance.h:32` | – | The boundaries and target for an AeConstraintMode constraint |
| `libcamera::ipa::AgcMeanLuminance::AgcConstraint::Bound` | `src/ipa/libipa/agc_mean_luminance.h:33` | – | 확인 필요 |
| `libcamera::ipa::AgcMeanLuminance::Params` | `src/ipa/libipa/agc_mean_luminance.h:64` | – | Collection of parameters for the mean luminance AGC algorithm |
| `libcamera::ipa::AgcMeanLuminance::Result` | `src/ipa/libipa/agc_mean_luminance.h:74` | `libcamera::ipa::ExposureModeHelper::Result` | Collection of results of the mean luminance AGC algorithm |
| `libcamera::ipa::AgcMeanLuminance::Traits` | `src/ipa/libipa/agc_mean_luminance.h:43` | – | A collection of callbacks |
| `libcamera::ipa::Algorithm` | `src/ipa/libipa/algorithm.h:22` | – | The base class for all IPA algorithms |
| `libcamera::ipa::AlgorithmFactory` | `src/ipa/libipa/algorithm.h:85` | `libcamera::ipa::AlgorithmFactoryBase` | Registration of Algorithm classes and creation of instances |
| `libcamera::ipa::AlgorithmFactoryBase` | `src/ipa/libipa/algorithm.h:65` | – | 확인 필요 |
| `libcamera::ipa::AwbAlgorithm` | `src/ipa/libipa/awb.h:113` | `libcamera::ipa::AwbAlgorithmBase` | The libipa AWB algorithm |
| `libcamera::ipa::AwbAlgorithmBase` | `src/ipa/libipa/awb.h:69` | – | Base class for AwbAlgorithm for non-templated functions implementation |
| `libcamera::ipa::AwbAlgorithmBase::ModeConfig` | `src/ipa/libipa/awb.h:95` | – | 확인 필요 |
| `libcamera::ipa::AwbBayes` | `src/ipa/libipa/awb_bayes.h:25` | `libcamera::ipa::AwbImplementation` | Implementation of a bayesian auto white balance algorithm |
| `libcamera::ipa::AwbGrey` | `src/ipa/libipa/awb_grey.h:21` | `libcamera::ipa::AwbImplementation` | A Grey world auto white balance algorithm |
| `libcamera::ipa::AwbImplementation` | `src/ipa/libipa/awb.h:53` | – | Pure virtual base class for AWB algorithms implementations |
| `libcamera::ipa::AwbImplementation::Result` | `src/ipa/libipa/awb.h:56` | – | The result of an AWB computation |
| `libcamera::ipa::AwbStats` | `src/ipa/libipa/awb.h:44` | – | An abstraction class wrapping hardware-specific AWB statistics |
| `libcamera::ipa::CameraSensorHelper` | `src/ipa/libipa/camera_sensor_helper.h:23` | – | Base class for computing sensor tuning parameters using |
| `libcamera::ipa::CameraSensorHelper::AnalogueGainExp` | `src/ipa/libipa/camera_sensor_helper.h:42` | – | Analogue gain constants for the exponential gain model |
| `libcamera::ipa::CameraSensorHelper::AnalogueGainLinear` | `src/ipa/libipa/camera_sensor_helper.h:35` | – | Analogue gain constants for the linear gain model |
| `libcamera::ipa::CameraSensorHelperAr0144` | `src/ipa/libipa/camera_sensor_helper.cpp:383` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperAr0521` | `src/ipa/libipa/camera_sensor_helper.cpp:473` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperFactory` | `src/ipa/libipa/camera_sensor_helper.h:75` | `libcamera::ipa::CameraSensorHelperFactoryBase` | Registration of CameraSensorHelperFactory classes and creation of instances |
| `libcamera::ipa::CameraSensorHelperFactoryBase` | `src/ipa/libipa/camera_sensor_helper.h:54` | – | Base class for camera sensor helper factories |
| `libcamera::ipa::CameraSensorHelperGc05a2` | `src/ipa/libipa/camera_sensor_helper.cpp:498` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperGc08a3` | `src/ipa/libipa/camera_sensor_helper.cpp:510` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperHm1246` | `src/ipa/libipa/camera_sensor_helper.cpp:522` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx214` | `src/ipa/libipa/camera_sensor_helper.cpp:532` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx219` | `src/ipa/libipa/camera_sensor_helper.cpp:544` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx258` | `src/ipa/libipa/camera_sensor_helper.cpp:556` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx283` | `src/ipa/libipa/camera_sensor_helper.cpp:568` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx290` | `src/ipa/libipa/camera_sensor_helper.cpp:580` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx296` | `src/ipa/libipa/camera_sensor_helper.cpp:592` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx327` | `src/ipa/libipa/camera_sensor_helper.cpp:602` | `libcamera::ipa::CameraSensorHelperImx290` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx335` | `src/ipa/libipa/camera_sensor_helper.cpp:607` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx355` | `src/ipa/libipa/camera_sensor_helper.cpp:619` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx415` | `src/ipa/libipa/camera_sensor_helper.cpp:631` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx462` | `src/ipa/libipa/camera_sensor_helper.cpp:641` | `libcamera::ipa::CameraSensorHelperImx290` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx471` | `src/ipa/libipa/camera_sensor_helper.cpp:646` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx477` | `src/ipa/libipa/camera_sensor_helper.cpp:659` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx662` | `src/ipa/libipa/camera_sensor_helper.cpp:669` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx678` | `src/ipa/libipa/camera_sensor_helper.cpp:681` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperImx708` | `src/ipa/libipa/camera_sensor_helper.cpp:693` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperMira220` | `src/ipa/libipa/camera_sensor_helper.cpp:739` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv01a10` | `src/ipa/libipa/camera_sensor_helper.cpp:704` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv08d10` | `src/ipa/libipa/camera_sensor_helper.cpp:716` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv08x40` | `src/ipa/libipa/camera_sensor_helper.cpp:728` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv13858` | `src/ipa/libipa/camera_sensor_helper.cpp:880` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv2685` | `src/ipa/libipa/camera_sensor_helper.cpp:751` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv2740` | `src/ipa/libipa/camera_sensor_helper.cpp:765` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv4689` | `src/ipa/libipa/camera_sensor_helper.cpp:777` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv5640` | `src/ipa/libipa/camera_sensor_helper.cpp:789` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv5647` | `src/ipa/libipa/camera_sensor_helper.cpp:801` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv5670` | `src/ipa/libipa/camera_sensor_helper.cpp:811` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv5675` | `src/ipa/libipa/camera_sensor_helper.cpp:821` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv5693` | `src/ipa/libipa/camera_sensor_helper.cpp:833` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv64a40` | `src/ipa/libipa/camera_sensor_helper.cpp:844` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv8858` | `src/ipa/libipa/camera_sensor_helper.cpp:854` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperOv8865` | `src/ipa/libipa/camera_sensor_helper.cpp:870` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperVd55g1` | `src/ipa/libipa/camera_sensor_helper.cpp:890` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CameraSensorHelperVd56g3` | `src/ipa/libipa/camera_sensor_helper.cpp:902` | `libcamera::ipa::CameraSensorHelper` | 확인 필요 |
| `libcamera::ipa::CcmAlgorithm` | `src/ipa/libipa/ccm.h:57` | `libcamera::ipa::CcmAlgorithmBase` | The libipa CCM algorithm |
| `libcamera::ipa::CcmAlgorithmBase` | `src/ipa/libipa/ccm.h:38` | – | Base class for CcmAlgorithm for non-templated functions implementation |
| `libcamera::ipa::ExposureModeHelper` | `src/ipa/libipa/exposure_mode_helper.h:22` | – | Class for splitting exposure into exposure time and total gain |
| `libcamera::ipa::ExposureModeHelper::Result` | `src/ipa/libipa/exposure_mode_helper.h:32` | – | Result of splitExposure() |
| `libcamera::ipa::FCQueue` | `src/ipa/libipa/fc_queue.h:32` | – | A support class for managing FrameContext instances in IPA modules |
| `libcamera::ipa::FixedPointQTraits` | `src/ipa/libipa/fixedpoint.h:20` | – | Traits type implementing fixed-point quantization conversions |
| `libcamera::ipa::FrameContext` | `src/ipa/libipa/fc_queue.h:24` | – | Context for a frame |
| `libcamera::ipa::GammaAlgorithm` | `src/ipa/libipa/gamma.h:64` | `libcamera::ipa::GammaAlgorithmBase` | The libipa gamma correction algorithm |
| `libcamera::ipa::GammaAlgorithmBase` | `src/ipa/libipa/gamma.h:41` | – | Base class for GammaAlgorithm to implement non-templated functions |
| `libcamera::ipa::Histogram` | `src/ipa/libipa/histogram.h:22` | – | The base class for creating histograms |
| `libcamera::ipa::Interpolator` | `src/ipa/libipa/interpolator.h:27` | – | Class for storing, retrieving, and interpolating objects |
| `libcamera::ipa::LscAlgorithm` | `src/ipa/libipa/lsc.h:78` | `libcamera::ipa::LscAlgorithmBase` | libIPA LSC algorithm implementation |
| `libcamera::ipa::LscAlgorithmBase` | `src/ipa/libipa/lsc.h:60` | – | Base class for LscAlgorithm |
| `libcamera::ipa::LscDescriptor` | `src/ipa/libipa/lsc_base.h:25` | – | Describe the ISP LSC engine |
| `libcamera::ipa::LscImplementation` | `src/ipa/libipa/lsc_base.h:32` | – | Pure virtual base class for LSC algorithm implementations |
| `libcamera::ipa::LscPolynomial` | `src/ipa/libipa/lsc_polynomial.h:52` | `libcamera::ipa::LscImplementation` | Radial Polynomial LSC algorithm implementation |
| `libcamera::ipa::LscTable` | `src/ipa/libipa/lsc_table.h:25` | `libcamera::ipa::LscImplementation` | Table based LSC algorithm implementation |
| `libcamera::ipa::Lux` | `src/ipa/libipa/lux.h:21` | – | Class that implements lux estimation |
| `libcamera::ipa::Module` | `src/ipa/libipa/module.h:30` | `libcamera::Loggable` | The base class for all IPA modules |
| `libcamera::ipa::Pwl` | `src/ipa/libipa/pwl.h:21` | – | Describe a univariate piecewise linear function in two-dimensional |
| `libcamera::ipa::Pwl::Interval` | `src/ipa/libipa/pwl.h:26` | – | Describe an interval in one-dimensional real space |
| `libcamera::ipa::Quantized` | `src/ipa/libipa/quantized.h:21` | – | Wrapper that stores a value in both quantized and floating-point form |
| `libcamera::ipa::V4L2Params` | `src/ipa/libipa/v4l2_params.h:91` | `libcamera::ipa::V4L2ParamsBase` | Helper class that represent an ISP configuration buffer |
| `libcamera::ipa::V4L2ParamsBase` | `src/ipa/libipa/v4l2_params.h:72` | – | Base class for V4L2Params |
| `libcamera::ipa::V4L2ParamsBlock` | `src/ipa/libipa/v4l2_params.h:27` | – | Helper class that represents an ISP configuration block |
| `libcamera::ipa::V4L2Stats` | `src/ipa/libipa/v4l2_stats.h:38` | `libcamera::ipa::V4L2StatsBase` | Helper class that represents an ISP statistics buffer |
| `libcamera::ipa::V4L2StatsBase` | `src/ipa/libipa/v4l2_stats.h:20` | – | Base class for V4L2Stats |
| `libcamera::ipa::agc::ActiveState` | `src/ipa/libipa/agc.h:55` | – | Active state for AgcAlgorithm |
| `libcamera::ipa::agc::ActiveState::(unnamed struct at src/ipa/libipa/agc.h:56:2)` | `src/ipa/libipa/agc.h:56` | – | 확인 필요 |
| `libcamera::ipa::agc::ActiveState::(unnamed struct at src/ipa/libipa/agc.h:60:2)` | `src/ipa/libipa/agc.h:60` | – | 확인 필요 |
| `libcamera::ipa::agc::FrameContext` | `src/ipa/libipa/agc.h:77` | – | 확인 필요 |
| `libcamera::ipa::agc::Session` | `src/ipa/libipa/agc.h:38` | – | Session configuration for AgcAlgorithm |
| `libcamera::ipa::agc::Session::(unnamed struct at src/ipa/libipa/agc.h:48:2)` | `src/ipa/libipa/agc.h:48` | – | 확인 필요 |
| `libcamera::ipa::awb::ActiveState` | `src/ipa/libipa/awb.h:31` | – | Active AWB state shared across frames |
| `libcamera::ipa::awb::Context` | `src/ipa/libipa/awb.h:26` | – | AWB gains and colour temperature |
| `libcamera::ipa::awb::FrameContext` | `src/ipa/libipa/awb.h:38` | `libcamera::ipa::awb::Context` | 확인 필요 |
| `libcamera::ipa::ccm::ActiveState` | `src/ipa/libipa/ccm.h:29` | – | Active CCM state |
| `libcamera::ipa::ccm::CcmContext` | `src/ipa/libipa/ccm.h:24` | – | CCM coefficients and offsets |
| `libcamera::ipa::gamma::ActiveState` | `src/ipa/libipa/gamma.h:30` | – | Active gamma correction algorithm state |
| `libcamera::ipa::gamma::FrameContext` | `src/ipa/libipa/gamma.h:34` | – | 확인 필요 |
| `libcamera::ipa::lsc::ActiveState` | `src/ipa/libipa/lsc.h:27` | – | The LSC active state |
| `libcamera::ipa::lsc::FrameContext` | `src/ipa/libipa/lsc.h:31` | – | 확인 필요 |
| `libcamera::ipa::lsc::Polynomial` | `src/ipa/libipa/lsc_polynomial.h:26` | – | Class for handling even polynomials used in lens shading correction |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::ipa::agc::extractControls` | – | `src/ipa/libipa/agc.h:97` | 확인 필요 |
| `libcamera::ipa::agc::prepareControls` | – | `src/ipa/libipa/agc.h:109` | 확인 필요 |
| `libcamera::ipa::calculateMSV` | – | `src/ipa/libipa/agc_msv.cpp:129` | 확인 필요 |
| `libcamera::ipa::details::qtype` | – | `src/ipa/libipa/fixedpoint.h:88` | 확인 필요 |
| `libcamera::ipa::estimateCCT` | `src/ipa/libipa/colours.h:19` | `src/ipa/libipa/colours.cpp:59` | Estimate correlated colour temperature from RGB color space input |
| `libcamera::ipa::expGainDb` | – | `src/ipa/libipa/camera_sensor_helper.cpp:367` | Helper function to compute the m parameter of the exponential gain model when the gain code is expressed in dB. |
| `libcamera::ipa::interpolateVector` | – | `src/ipa/libipa/lsc.cpp:85` | 확인 필요 |
| `libcamera::ipa::logCategoryAgc` | `src/ipa/libipa/agc.cpp:40` | – | 확인 필요 |
| `libcamera::ipa::logCategoryAgcMSV` | `src/ipa/libipa/agc_msv.cpp:22` | – | 확인 필요 |
| `libcamera::ipa::logCategoryCcm` | `src/ipa/libipa/ccm.cpp:19` | – | 확인 필요 |
| `libcamera::ipa::logCategoryGamma` | `src/ipa/libipa/gamma.h:26` | – | 확인 필요 |
| `libcamera::ipa::logCategoryV4L2Params` | `src/ipa/libipa/v4l2_params.h:24` | – | 확인 필요 |
| `libcamera::ipa::logCategoryV4L2Stats` | `src/ipa/libipa/v4l2_stats.cpp:16` | – | 확인 필요 |
| `libcamera::ipa::rec601LuminanceFromRGB` | `src/ipa/libipa/colours.h:18` | `src/ipa/libipa/colours.cpp:32` | Estimate luminance from RGB values following ITU-R BT.601 |
| `libcamera::logCategoryAgcMeanLuminance` | `src/ipa/libipa/agc_mean_luminance.cpp:32` | – | 확인 필요 |
| `libcamera::logCategoryAwb` | `src/ipa/libipa/awb_bayes.cpp:59` | – | 확인 필요 |
| `libcamera::logCategoryCameraSensorHelper` | `src/ipa/libipa/camera_sensor_helper.cpp:30` | – | 확인 필요 |
| `libcamera::logCategoryExposureModeHelper` | `src/ipa/libipa/exposure_mode_helper.cpp:26` | – | 확인 필요 |
| `libcamera::logCategoryFCQueue` | `src/ipa/libipa/fc_queue.h:17` | – | 확인 필요 |
| `libcamera::logCategoryIPAModuleAlgo` | `src/ipa/libipa/module.h:24` | – | 확인 필요 |
| `libcamera::logCategoryInterpolator` | `src/ipa/libipa/interpolator.h:22` | – | 확인 필요 |
| `libcamera::logCategoryLsc` | `src/ipa/libipa/lsc.cpp:24` | – | 확인 필요 |
| `libcamera::logCategoryLscPolynomial` | `src/ipa/libipa/lsc_polynomial.cpp:22` | – | 확인 필요 |
| `libcamera::logCategoryLscTable` | `src/ipa/libipa/lsc_table.h:21` | – | 확인 필요 |
| `libcamera::logCategoryLux` | `src/ipa/libipa/lux.cpp:32` | – | 확인 필요 |

## src/ipa/mali-c55

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::ipa::mali_c55::Algorithm` | `src/ipa/mali-c55/algorithms/algorithm.h:20` | `libcamera::ipa::Algorithm` | 확인 필요 |
| `libcamera::ipa::mali_c55::IPAActiveState` | `src/ipa/mali-c55/ipa_context.h:39` | – | Active state for algorithms |
| `libcamera::ipa::mali_c55::IPAActiveState::Agc` | `src/ipa/mali-c55/ipa_context.h:40` | `libcamera::ipa::agc::ActiveState` | 확인 필요 |
| `libcamera::ipa::mali_c55::IPAContext` | `src/ipa/mali-c55/ipa_context.h:62` | – | Global IPA context data shared between all algorithms |
| `libcamera::ipa::mali_c55::IPAFrameContext` | `src/ipa/mali-c55/ipa_context.h:49` | `libcamera::ipa::FrameContext` | Per-frame context for algorithms |
| `libcamera::ipa::mali_c55::IPAFrameContext::(unnamed struct at src/ipa/mali-c55/ipa_context.h:52:2)` | `src/ipa/mali-c55/ipa_context.h:52` | – | 확인 필요 |
| `libcamera::ipa::mali_c55::IPAMaliC55` | `src/ipa/mali-c55/mali-c55.cpp:46` | `libcamera::ipa::mali_c55::IPAMaliC55Interface`, `libcamera::ipa::mali_c55::Module` | 확인 필요 |
| `libcamera::ipa::mali_c55::IPASessionConfiguration` | `src/ipa/mali-c55/ipa_context.h:30` | – | Session configuration for the IPA module |
| `libcamera::ipa::mali_c55::IPASessionConfiguration::(unnamed struct at src/ipa/mali-c55/ipa_context.h:33:2)` | `src/ipa/mali-c55/ipa_context.h:33` | – | 확인 필요 |
| `libcamera::ipa::mali_c55::MaliC55Blocks` | `src/ipa/mali-c55/params.h:21` | – | 확인 필요 |
| `libcamera::ipa::mali_c55::MaliC55Params` | `src/ipa/mali-c55/params.h:70` | `libcamera::ipa::V4L2Params` | 확인 필요 |
| `libcamera::ipa::mali_c55::algorithms::Agc` | `src/ipa/mali-c55/algorithms/agc.h:46` | `libcamera::ipa::mali_c55::Algorithm` | 확인 필요 |
| `libcamera::ipa::mali_c55::algorithms::AgcStatistics` | `src/ipa/mali-c55/algorithms/agc.h:24` | – | 확인 필요 |
| `libcamera::ipa::mali_c55::algorithms::AgcTraits` | `src/ipa/mali-c55/algorithms/agc.cpp:224` | `libcamera::ipa::AgcMeanLuminance::Traits` | 확인 필요 |
| `libcamera::ipa::mali_c55::algorithms::Awb` | `src/ipa/mali-c55/algorithms/awb.h:29` | `libcamera::ipa::mali_c55::Algorithm` | 확인 필요 |
| `libcamera::ipa::mali_c55::algorithms::BlackLevelCorrection` | `src/ipa/mali-c55/algorithms/blc.h:15` | `libcamera::ipa::mali_c55::Algorithm` | MaliC55 Black Level Correction control |
| `libcamera::ipa::mali_c55::algorithms::Ccm` | `src/ipa/mali-c55/algorithms/ccm.h:27` | `libcamera::ipa::mali_c55::Algorithm` | Mali-C55 color correction matrix algorithm |
| `libcamera::ipa::mali_c55::algorithms::Lsc` | `src/ipa/mali-c55/algorithms/lsc.h:26` | `libcamera::ipa::mali_c55::Algorithm` | 확인 필요 |
| `libcamera::ipa::mali_c55::algorithms::MaliC55AwbStats` | `src/ipa/mali-c55/algorithms/awb.cpp:26` | `libcamera::ipa::AwbStats` | 확인 필요 |
| `libcamera::ipa::mali_c55::details::block_type` | `src/ipa/mali-c55/params.h:38` | – | 확인 필요 |
| `libcamera::ipa::mali_c55::details::param_traits` | `src/ipa/mali-c55/params.h:61` | – | 확인 필요 |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::ipa::mali_c55::algorithms::logCategoryMaliC55Agc` | `src/ipa/mali-c55/algorithms/agc.cpp:25` | – | 확인 필요 |
| `libcamera::ipa::mali_c55::algorithms::logCategoryMaliC55Awb` | `src/ipa/mali-c55/algorithms/awb.cpp:21` | – | 확인 필요 |
| `libcamera::ipa::mali_c55::algorithms::logCategoryMaliC55Blc` | `src/ipa/mali-c55/algorithms/blc.cpp:28` | – | MaliC55 Black Level Correction control |
| `libcamera::ipa::mali_c55::algorithms::logCategoryMaliC55Ccm` | `src/ipa/mali-c55/algorithms/ccm.cpp:21` | – | 확인 필요 |
| `libcamera::ipa::mali_c55::algorithms::logCategoryMaliC55Lsc` | `src/ipa/mali-c55/algorithms/lsc.cpp:17` | – | 확인 필요 |
| `libcamera::logCategoryIPAMaliC55` | `src/ipa/mali-c55/mali-c55.cpp:37` | – | 확인 필요 |

## src/ipa/rkisp1

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::ipa::rkisp1::Algorithm` | `src/ipa/rkisp1/algorithms/algorithm.h:18` | `libcamera::ipa::Algorithm` | 확인 필요 |
| `libcamera::ipa::rkisp1::BlockType` | `src/ipa/rkisp1/params.h:21` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::BlockTypeInfo` | `src/ipa/rkisp1/params.cpp:28` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAActiveState` | `src/ipa/rkisp1/ipa_context.h:79` | – | Active state for algorithms |
| `libcamera::ipa::rkisp1::IPAActiveState::(unnamed struct at src/ipa/rkisp1/ipa_context.h:101:2)` | `src/ipa/rkisp1/ipa_context.h:101` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAActiveState::(unnamed struct at src/ipa/rkisp1/ipa_context.h:108:2)` | `src/ipa/rkisp1/ipa_context.h:108` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAActiveState::(unnamed struct at src/ipa/rkisp1/ipa_context.h:112:2)` | `src/ipa/rkisp1/ipa_context.h:112` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAActiveState::(unnamed struct at src/ipa/rkisp1/ipa_context.h:88:2)` | `src/ipa/rkisp1/ipa_context.h:88` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAActiveState::(unnamed struct at src/ipa/rkisp1/ipa_context.h:97:2)` | `src/ipa/rkisp1/ipa_context.h:97` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAActiveState::Agc` | `src/ipa/rkisp1/ipa_context.h:80` | `libcamera::ipa::agc::ActiveState` | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAContext` | `src/ipa/rkisp1/ipa_context.h:178` | – | Global IPA context data shared between all algorithms |
| `libcamera::ipa::rkisp1::IPAFrameContext` | `src/ipa/rkisp1/ipa_context.h:122` | `libcamera::ipa::FrameContext` | Per-frame context for algorithms |
| `libcamera::ipa::rkisp1::IPAFrameContext::(unnamed struct at src/ipa/rkisp1/ipa_context.h:130:2)` | `src/ipa/rkisp1/ipa_context.h:130` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAFrameContext::(unnamed struct at src/ipa/rkisp1/ipa_context.h:140:2)` | `src/ipa/rkisp1/ipa_context.h:140` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAFrameContext::(unnamed struct at src/ipa/rkisp1/ipa_context.h:145:2)` | `src/ipa/rkisp1/ipa_context.h:145` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAFrameContext::(unnamed struct at src/ipa/rkisp1/ipa_context.h:150:2)` | `src/ipa/rkisp1/ipa_context.h:150` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAFrameContext::(unnamed struct at src/ipa/rkisp1/ipa_context.h:158:2)` | `src/ipa/rkisp1/ipa_context.h:158` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAFrameContext::(unnamed struct at src/ipa/rkisp1/ipa_context.h:165:2)` | `src/ipa/rkisp1/ipa_context.h:165` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAFrameContext::(unnamed struct at src/ipa/rkisp1/ipa_context.h:169:2)` | `src/ipa/rkisp1/ipa_context.h:169` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAFrameContext::Agc` | `src/ipa/rkisp1/ipa_context.h:123` | `libcamera::ipa::agc::FrameContext` | 확인 필요 |
| `libcamera::ipa::rkisp1::IPAHwSettings` | `src/ipa/rkisp1/ipa_context.h:46` | – | RkISP1 version-specific hardware parameters |
| `libcamera::ipa::rkisp1::IPARkISP1` | `src/ipa/rkisp1/rkisp1.cpp:46` | `libcamera::ipa::rkisp1::IPARkISP1Interface`, `libcamera::ipa::rkisp1::Module` | 확인 필요 |
| `libcamera::ipa::rkisp1::IPASessionConfiguration` | `src/ipa/rkisp1/ipa_context.h:60` | – | Session configuration for the IPA module |
| `libcamera::ipa::rkisp1::IPASessionConfiguration::(unnamed struct at src/ipa/rkisp1/ipa_context.h:67:2)` | `src/ipa/rkisp1/ipa_context.h:67` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPASessionConfiguration::(unnamed struct at src/ipa/rkisp1/ipa_context.h:71:2)` | `src/ipa/rkisp1/ipa_context.h:71` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::IPASessionConfiguration::Agc` | `src/ipa/rkisp1/ipa_context.h:61` | `libcamera::ipa::agc::Session` | 확인 필요 |
| `libcamera::ipa::rkisp1::RKISP1AwbSession` | `src/ipa/rkisp1/ipa_context.h:55` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::RkISP1Params` | `src/ipa/rkisp1/params.h:93` | `libcamera::ipa::V4L2Params` | 확인 필요 |
| `libcamera::ipa::rkisp1::RkISP1ParamsBlock` | `src/ipa/rkisp1/params.h:125` | `libcamera::ipa::V4L2ParamsBlock` | 확인 필요 |
| `libcamera::ipa::rkisp1::algorithms::Agc` | `src/ipa/rkisp1/algorithms/agc.h:24` | `libcamera::ipa::rkisp1::Algorithm` | A mean-based auto-exposure algorithm |
| `libcamera::ipa::rkisp1::algorithms::AgcTraits` | `src/ipa/rkisp1/algorithms/agc.cpp:276` | `libcamera::ipa::AgcMeanLuminance::Traits` | 확인 필요 |
| `libcamera::ipa::rkisp1::algorithms::Awb` | `src/ipa/rkisp1/algorithms/awb.h:29` | `libcamera::ipa::rkisp1::Algorithm` | Manage the white balance with automatic and manual controls |
| `libcamera::ipa::rkisp1::algorithms::BlackLevelCorrection` | `src/ipa/rkisp1/algorithms/blc.h:16` | `libcamera::ipa::rkisp1::Algorithm` | RkISP1 Black Level Correction control |
| `libcamera::ipa::rkisp1::algorithms::Ccm` | `src/ipa/rkisp1/algorithms/ccm.h:27` | `libcamera::ipa::rkisp1::Algorithm` | RkISP1 color correction matrix algorithm |
| `libcamera::ipa::rkisp1::algorithms::ColorProcessing` | `src/ipa/rkisp1/algorithms/cproc.h:18` | `libcamera::ipa::rkisp1::Algorithm` | RkISP1 Color Processing control |
| `libcamera::ipa::rkisp1::algorithms::Compress` | `src/ipa/rkisp1/algorithms/compress.h:16` | `libcamera::ipa::rkisp1::Algorithm` | RkISP1 Compress curve |
| `libcamera::ipa::rkisp1::algorithms::DefectPixelClusterCorrection` | `src/ipa/rkisp1/algorithms/dpcc.h:16` | `libcamera::ipa::rkisp1::Algorithm` | RkISP1 Defect Pixel Cluster Correction control |
| `libcamera::ipa::rkisp1::algorithms::Dpf` | `src/ipa/rkisp1/algorithms/dpf.h:18` | `libcamera::ipa::rkisp1::Algorithm` | RkISP1 Denoise Pre-Filter control |
| `libcamera::ipa::rkisp1::algorithms::Filter` | `src/ipa/rkisp1/algorithms/filter.h:18` | `libcamera::ipa::rkisp1::Algorithm` | RkISP1 Filter control |
| `libcamera::ipa::rkisp1::algorithms::GammaOutCorrection` | `src/ipa/rkisp1/algorithms/goc.h:21` | `libcamera::ipa::rkisp1::Algorithm` | RkISP1 Gamma out correction |
| `libcamera::ipa::rkisp1::algorithms::GammaSensorLinearization` | `src/ipa/rkisp1/algorithms/gsl.h:16` | `libcamera::ipa::rkisp1::Algorithm` | RkISP1 Gamma Sensor Linearization control |
| `libcamera::ipa::rkisp1::algorithms::LensShadingCorrection` | `src/ipa/rkisp1/algorithms/lsc.h:25` | `libcamera::ipa::rkisp1::Algorithm` | RkISP1 Lens Shading Correction control |
| `libcamera::ipa::rkisp1::algorithms::Lux` | `src/ipa/rkisp1/algorithms/lux.h:20` | `libcamera::ipa::rkisp1::Algorithm` | RkISP1 Lux control |
| `libcamera::ipa::rkisp1::algorithms::RkISP1AwbStats` | `src/ipa/rkisp1/algorithms/awb.cpp:28` | `libcamera::ipa::AwbStats` | 확인 필요 |
| `libcamera::ipa::rkisp1::algorithms::WideDynamicRange` | `src/ipa/rkisp1/algorithms/wdr.h:20` | `libcamera::ipa::rkisp1::Algorithm` | RkISP1 Wide Dynamic Range algorithm |
| `libcamera::ipa::rkisp1::details::block_type` | `src/ipa/rkisp1/params.h:48` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::details::params_traits` | `src/ipa/rkisp1/params.h:81` | – | 확인 필요 |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::ipa::rkisp1::algorithms::applyRequestedBrightness` | – | `src/ipa/rkisp1/algorithms/cproc.cpp:49` | 확인 필요 |
| `libcamera::ipa::rkisp1::algorithms::logCategoryRkISP1Agc` | `src/ipa/rkisp1/algorithms/agc.cpp:35` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::algorithms::logCategoryRkISP1Awb` | `src/ipa/rkisp1/algorithms/awb.cpp:26` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::algorithms::logCategoryRkISP1Blc` | `src/ipa/rkisp1/algorithms/blc.cpp:40` | – | RkISP1 Black Level Correction control |
| `libcamera::ipa::rkisp1::algorithms::logCategoryRkISP1CProc` | `src/ipa/rkisp1/algorithms/cproc.cpp:34` | – | RkISP1 Color Processing control |
| `libcamera::ipa::rkisp1::algorithms::logCategoryRkISP1Ccm` | `src/ipa/rkisp1/algorithms/ccm.cpp:35` | – | RkISP1 color correction matrix algorithm |
| `libcamera::ipa::rkisp1::algorithms::logCategoryRkISP1Compress` | `src/ipa/rkisp1/algorithms/compress.cpp:42` | – | RkISP1 Compress curve |
| `libcamera::ipa::rkisp1::algorithms::logCategoryRkISP1Dpcc` | `src/ipa/rkisp1/algorithms/dpcc.cpp:37` | – | RkISP1 Defect Pixel Cluster Correction control |
| `libcamera::ipa::rkisp1::algorithms::logCategoryRkISP1Dpf` | `src/ipa/rkisp1/algorithms/dpf.cpp:38` | – | RkISP1 Denoise Pre-Filter control |
| `libcamera::ipa::rkisp1::algorithms::logCategoryRkISP1Filter` | `src/ipa/rkisp1/algorithms/filter.cpp:37` | – | RkISP1 Filter control |
| `libcamera::ipa::rkisp1::algorithms::logCategoryRkISP1Gamma` | `src/ipa/rkisp1/algorithms/goc.cpp:37` | – | RkISP1 Gamma out correction |
| `libcamera::ipa::rkisp1::algorithms::logCategoryRkISP1Gsl` | `src/ipa/rkisp1/algorithms/gsl.cpp:47` | – | RkISP1 Gamma Sensor Linearization control |
| `libcamera::ipa::rkisp1::algorithms::logCategoryRkISP1Lsc` | `src/ipa/rkisp1/algorithms/lsc.cpp:26` | – | 확인 필요 |
| `libcamera::ipa::rkisp1::algorithms::logCategoryRkISP1Wdr` | `src/ipa/rkisp1/algorithms/wdr.cpp:91` | – | RkISP1 Wide Dynamic Range algorithm |
| `libcamera::ipa::rkisp1::algorithms::parseSizes` | – | `src/ipa/rkisp1/algorithms/lsc.cpp:32` | 확인 필요 |
| `libcamera::ipa::rkisp1::algorithms::quantize` | – | `src/ipa/rkisp1/algorithms/lsc.cpp:88` | 확인 필요 |
| `libcamera::ipa::rkisp1::algorithms::sizesListToPositions` | – | `src/ipa/rkisp1/algorithms/lsc.cpp:72` | The rkisp1 LSC grid spacing is defined by the cell sizes on the top-left quadrant of the grid. This is then mirrored in hardware to the other quadrants. See parseSizes() for further details. For easie |
| `libcamera::logCategoryIPARkISP1` | `src/ipa/rkisp1/rkisp1.cpp:39` | – | 확인 필요 |
| `libcamera::logCategoryRkISP1Params` | `src/ipa/rkisp1/params.cpp:22` | – | 확인 필요 |

## src/ipa/rpi

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `AfPauseState` | `src/ipa/rpi/controller/af_status.h:23` | – | 확인 필요 |
| `AfState` | `src/ipa/rpi/controller/af_status.h:16` | – | The AF algorithm should post the following structure into the image's "af.status" metadata. lensSetting should control the lens. |
| `AfStatus` | `src/ipa/rpi/controller/af_status.h:29` | – | 확인 필요 |
| `AgcPrepareStatus` | `src/ipa/rpi/controller/agc_status.h:46` | – | 확인 필요 |
| `AgcStatus` | `src/ipa/rpi/controller/agc_status.h:28` | – | Note: total_exposure_value will be reported as zero until the algorithm has seen statistics and calculated meaningful values. The contents should be ignored until then. |
| `AlscStatus` | `src/ipa/rpi/controller/alsc_status.h:16` | – | The ALSC algorithm should post the following structure into the image's "alsc.status" metadata. |
| `AwbStatus` | `src/ipa/rpi/controller/awb_status.h:14` | – | The AWB algorithm places its results into both the image and global metadata, under the tag "awb.status". |
| `BlackLevelStatus` | `src/ipa/rpi/controller/black_level_status.h:11` | – | The "black level" algorithm stores the black levels to use. |
| `CacStatus` | `src/ipa/rpi/controller/cac_status.h:9` | – | 확인 필요 |
| `CamHelperImx219` | `src/ipa/rpi/cam_helper/cam_helper_imx219.cpp:43` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperImx283` | `src/ipa/rpi/cam_helper/cam_helper_imx283.cpp:16` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperImx290` | `src/ipa/rpi/cam_helper/cam_helper_imx290.cpp:16` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperImx296` | `src/ipa/rpi/cam_helper/cam_helper_imx296.cpp:33` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperImx355` | `src/ipa/rpi/cam_helper/cam_helper_imx355.cpp:19` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperImx415` | `src/ipa/rpi/cam_helper/cam_helper_imx415.cpp:16` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperImx477` | `src/ipa/rpi/cam_helper/cam_helper_imx477.cpp:47` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperImx519` | `src/ipa/rpi/cam_helper/cam_helper_imx519.cpp:47` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperImx708` | `src/ipa/rpi/cam_helper/cam_helper_imx708.cpp:49` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperMira220` | `src/ipa/rpi/cam_helper/cam_helper_mira220.cpp:16` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperOv5647` | `src/ipa/rpi/cam_helper/cam_helper_ov5647.cpp:16` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperOv64a40` | `src/ipa/rpi/cam_helper/cam_helper_ov64a40.cpp:17` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperOv7251` | `src/ipa/rpi/cam_helper/cam_helper_ov7251.cpp:16` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperOv9281` | `src/ipa/rpi/cam_helper/cam_helper_ov9281.cpp:16` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperStarvis2` | `src/ipa/rpi/cam_helper/cam_helper_starvis2.cpp:17` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperVd55g1` | `src/ipa/rpi/cam_helper/cam_helper_vd55g1.cpp:16` | `RPiController::CamHelper` | 확인 필요 |
| `CamHelperVd56g3` | `src/ipa/rpi/cam_helper/cam_helper_vd56g3.cpp:16` | `RPiController::CamHelper` | 확인 필요 |
| `CameraMode` | `src/ipa/rpi/controller/camera_mode.h:19` | – | Description of a "camera mode", holding enough information for control algorithms to adapt their behaviour to the different modes of the camera, including binning, scaling, cropping etc. |
| `CcmStatus` | `src/ipa/rpi/controller/ccm_status.h:11` | – | The "ccm" algorithm generates an appropriate colour matrix. |
| `CdnStatus` | `src/ipa/rpi/controller/denoise_status.h:26` | – | 확인 필요 |
| `ContrastStatus` | `src/ipa/rpi/controller/contrast_status.h:16` | – | The "contrast" algorithm creates a gamma curve, optionally doing a little bit of contrast stretching based on the AGC histogram. |
| `DecompandStatus` | `src/ipa/rpi/controller/decompand_status.h:6` | – | 확인 필요 |
| `DenoiseStatus` | `src/ipa/rpi/controller/denoise_status.h:11` | – | This stores the parameters required for Denoise. |
| `DeviceStatus` | `src/ipa/rpi/controller/device_status.h:19` | – | Definition of "device metadata" which stores things like exposure time and analogue gain that downstream control algorithms will want to know. |
| `DpcStatus` | `src/ipa/rpi/controller/dpc_status.h:11` | – | The "DPC" algorithm sets defective pixel correction strength. |
| `GeqStatus` | `src/ipa/rpi/controller/geq_status.h:11` | – | The "GEQ" algorithm calculates the green equalisation thresholds |
| `HdrStatus` | `src/ipa/rpi/controller/hdr_status.h:16` | – | The HDR algorithm process method should post an HdrStatus into the image metadata under the tag "hdr.status". |
| `LuxStatus` | `src/ipa/rpi/controller/lux_status.h:20` | – | The "lux" algorithm looks at the (AGC) histogram statistics of the frame and estimates the current lux level of the scene. It does this by a simple ratio calculation comparing to a reference image tha |
| `NoiseStatus` | `src/ipa/rpi/controller/noise_status.h:11` | – | The "noise" algorithm stores an estimate of the noise profile for this image. |
| `RPiController::Af` | `src/ipa/rpi/controller/rpi/af.h:44` | `RPiController::AfAlgorithm` | 확인 필요 |
| `RPiController::Af::CfgParams` | `src/ipa/rpi/controller/rpi/af.h:110` | – | 확인 필요 |
| `RPiController::Af::RangeDependentParams` | `src/ipa/rpi/controller/rpi/af.h:84` | – | 확인 필요 |
| `RPiController::Af::RegionWeights` | `src/ipa/rpi/controller/rpi/af.h:132` | – | 확인 필요 |
| `RPiController::Af::ScanRecord` | `src/ipa/rpi/controller/rpi/af.h:125` | – | 확인 필요 |
| `RPiController::Af::ScanState` | `src/ipa/rpi/controller/rpi/af.h:74` | – | 확인 필요 |
| `RPiController::Af::SpeedDependentParams` | `src/ipa/rpi/controller/rpi/af.h:93` | – | 확인 필요 |
| `RPiController::AfAlgorithm` | `src/ipa/rpi/controller/af_algorithm.h:16` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::AfAlgorithm::AfMode` | `src/ipa/rpi/controller/af_algorithm.h:50` | – | 확인 필요 |
| `RPiController::AfAlgorithm::AfPause` | `src/ipa/rpi/controller/af_algorithm.h:54` | – | 확인 필요 |
| `RPiController::AfAlgorithm::AfRange` | `src/ipa/rpi/controller/af_algorithm.h:41` | – | An autofocus algorithm should provide the following calls. |
| `RPiController::AfAlgorithm::AfSpeed` | `src/ipa/rpi/controller/af_algorithm.h:46` | – | 확인 필요 |
| `RPiController::Agc` | `src/ipa/rpi/controller/rpi/agc.h:25` | `RPiController::AgcAlgorithm` | 확인 필요 |
| `RPiController::AgcAlgorithm` | `src/ipa/rpi/controller/agc_algorithm.h:17` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::AgcChannel` | `src/ipa/rpi/controller/rpi/agc_channel.h:84` | – | 확인 필요 |
| `RPiController::AgcChannel::ExposureValues` | `src/ipa/rpi/controller/rpi/agc_channel.h:133` | – | 확인 필요 |
| `RPiController::AgcChannelConstraint` | `src/ipa/rpi/controller/rpi/agc_channel.h:50` | – | 확인 필요 |
| `RPiController::AgcChannelConstraint::Bound` | `src/ipa/rpi/controller/rpi/agc_channel.h:51` | – | 확인 필요 |
| `RPiController::AgcChannelData` | `src/ipa/rpi/controller/rpi/agc.h:19` | – | 확인 필요 |
| `RPiController::AgcConfig` | `src/ipa/rpi/controller/rpi/agc_channel.h:59` | – | 확인 필요 |
| `RPiController::AgcConstraint` | `src/ipa/rpi/controller/rpi/agc_channel.h:38` | – | 확인 필요 |
| `RPiController::AgcConstraint::Bound` | `src/ipa/rpi/controller/rpi/agc_channel.h:39` | – | 확인 필요 |
| `RPiController::AgcExposureMode` | `src/ipa/rpi/controller/rpi/agc_channel.h:32` | – | 확인 필요 |
| `RPiController::AgcMeteringMode` | `src/ipa/rpi/controller/rpi/agc_channel.h:27` | – | 확인 필요 |
| `RPiController::Algorithm` | `src/ipa/rpi/controller/algorithm.h:26` | – | This defines the basic interface for all control algorithms. |
| `RPiController::Alsc` | `src/ipa/rpi/controller/rpi/alsc.h:107` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::AlscCalibration` | `src/ipa/rpi/controller/rpi/alsc.h:79` | – | 확인 필요 |
| `RPiController::AlscConfig` | `src/ipa/rpi/controller/rpi/alsc.h:84` | – | 확인 필요 |
| `RPiController::Array2D` | `src/ipa/rpi/controller/rpi/alsc.h:32` | – | The Array2D class is a very thin wrapper round std::vector so that it can be used in exactly the same way in the code but carries its correct width and height ("dimensions") with it. |
| `RPiController::Awb` | `src/ipa/rpi/controller/rpi/awb.h:66` | `RPiController::AwbAlgorithm` | 확인 필요 |
| `RPiController::Awb::RGB` | `src/ipa/rpi/controller/rpi/awb.h:87` | – | 확인 필요 |
| `RPiController::AwbAlgorithm` | `src/ipa/rpi/controller/awb_algorithm.h:13` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::AwbBayes` | `src/ipa/rpi/controller/rpi/awb_bayes.cpp:78` | `RPiController::Awb` | 확인 필요 |
| `RPiController::AwbBayesConfig` | `src/ipa/rpi/controller/rpi/awb_bayes.cpp:49` | – | 확인 필요 |
| `RPiController::AwbConfig` | `src/ipa/rpi/controller/rpi/awb.h:25` | – | 확인 필요 |
| `RPiController::AwbMode` | `src/ipa/rpi/controller/rpi/awb.h:19` | – | 확인 필요 |
| `RPiController::AwbPrior` | `src/ipa/rpi/controller/rpi/awb_bayes.cpp:43` | – | 확인 필요 |
| `RPiController::BlackLevel` | `src/ipa/rpi/controller/rpi/black_level.h:16` | `RPiController::BlackLevelAlgorithm` | 확인 필요 |
| `RPiController::BlackLevelAlgorithm` | `src/ipa/rpi/controller/black_level_algorithm.h:13` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::Cac` | `src/ipa/rpi/controller/rpi/cac.h:22` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::CacConfig` | `src/ipa/rpi/controller/rpi/cac.h:14` | – | 확인 필요 |
| `RPiController::CamHelper` | `src/ipa/rpi/cam_helper/cam_helper.h:72` | – | The CamHelper class provides a number of facilities that anyone trying to drive a camera will need to know, but which are not provided by the standard driver framework. Specifically, it provides: |
| `RPiController::Ccm` | `src/ipa/rpi/controller/rpi/ccm.h:29` | `RPiController::CcmAlgorithm` | 확인 필요 |
| `RPiController::CcmAlgorithm` | `src/ipa/rpi/controller/ccm_algorithm.h:17` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::CcmConfig` | `src/ipa/rpi/controller/rpi/ccm.h:24` | – | 확인 필요 |
| `RPiController::Contrast` | `src/ipa/rpi/controller/rpi/contrast.h:33` | `RPiController::ContrastAlgorithm` | 확인 필요 |
| `RPiController::ContrastAlgorithm` | `src/ipa/rpi/controller/contrast_algorithm.h:13` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::ContrastConfig` | `src/ipa/rpi/controller/rpi/contrast.h:22` | – | Back End algorithm to appaly correct digital gain. Should be placed after Back End AWB. |
| `RPiController::Controller` | `src/ipa/rpi/controller/controller.h:38` | – | The Controller holds a pointer to some global_metadata, which is how different controllers and control algorithms within them can exchange information. The Prepare function returns a pointer to metada |
| `RPiController::Controller::HardwareConfig` | `src/ipa/rpi/controller/controller.h:41` | – | 확인 필요 |
| `RPiController::CtCcm` | `src/ipa/rpi/controller/rpi/ccm.h:19` | – | Algorithm to calculate colour matrix. Should be placed after AWB. |
| `RPiController::Decompand` | `src/ipa/rpi/controller/rpi/decompand.h:16` | `RPiController::DecompandAlgorithm` | 확인 필요 |
| `RPiController::DecompandAlgorithm` | `src/ipa/rpi/controller/decompand_algorithm.h:15` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::DecompandConfig` | `src/ipa/rpi/controller/rpi/decompand.h:11` | – | 확인 필요 |
| `RPiController::Denoise` | `src/ipa/rpi/controller/rpi/denoise.h:37` | `RPiController::DenoiseAlgorithm` | 확인 필요 |
| `RPiController::DenoiseAlgorithm` | `src/ipa/rpi/controller/denoise_algorithm.h:17` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::DenoiseConfig` | `src/ipa/rpi/controller/rpi/denoise.h:19` | – | Algorithm to calculate correct denoise settings. |
| `RPiController::DenoiseMode` | `src/ipa/rpi/controller/denoise_algorithm.h:15` | – | 확인 필요 |
| `RPiController::Dpc` | `src/ipa/rpi/controller/rpi/dpc.h:20` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::DpcConfig` | `src/ipa/rpi/controller/rpi/dpc.h:16` | – | Back End algorithm to apply appropriate GEQ settings. |
| `RPiController::Geq` | `src/ipa/rpi/controller/rpi/geq.h:24` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::GeqConfig` | `src/ipa/rpi/controller/rpi/geq.h:18` | – | Back End algorithm to apply appropriate GEQ settings. |
| `RPiController::Hdr` | `src/ipa/rpi/controller/rpi/hdr.h:58` | `RPiController::HdrAlgorithm` | 확인 필요 |
| `RPiController::HdrAlgorithm` | `src/ipa/rpi/controller/hdr_algorithm.h:15` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::HdrConfig` | `src/ipa/rpi/controller/rpi/hdr.h:24` | – | 확인 필요 |
| `RPiController::Histogram` | `src/ipa/rpi/controller/histogram.h:20` | – | 확인 필요 |
| `RPiController::Lux` | `src/ipa/rpi/controller/rpi/lux.h:21` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::MdParser` | `src/ipa/rpi/cam_helper/md_parser.h:59` | – | Abstract base class from which other metadata parsers are derived. |
| `RPiController::MdParser::Status` | `src/ipa/rpi/cam_helper/md_parser.h:70` | – | Parser status codes: OK - success NOTFOUND - value such as exposure or gain was not found ERROR - all other errors |
| `RPiController::MdParserSmia` | `src/ipa/rpi/cam_helper/md_parser.h:120` | `RPiController::MdParser` | This isn't a full implementation of a metadata parser for SMIA sensors, however, it does provide the findRegs function which will prove useful and make it easier to implement parsers for other SMIA-li |
| `RPiController::MdParserSmia::ParseStatus` | `src/ipa/rpi/cam_helper/md_parser.h:139` | – | Note that error codes > 0 are regarded as non-fatal; codes < 0 indicate a bad data buffer. Status codes are: ParseOk - found all registers, much happiness MissingRegs - some registers found; should th |
| `RPiController::Metadata` | `src/ipa/rpi/controller/metadata.h:21` | – | 확인 필요 |
| `RPiController::Noise` | `src/ipa/rpi/controller/rpi/noise.h:16` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::PdafData` | `src/ipa/rpi/controller/pdaf_data.h:15` | – | 확인 필요 |
| `RPiController::RegionStats` | `src/ipa/rpi/controller/region_stats.h:18` | – | 확인 필요 |
| `RPiController::RegionStats::Region` | `src/ipa/rpi/controller/region_stats.h:21` | – | 확인 필요 |
| `RPiController::RegisterAlgorithm` | `src/ipa/rpi/controller/algorithm.h:63` | – | 확인 필요 |
| `RPiController::RegisterCamHelper` | `src/ipa/rpi/cam_helper/cam_helper.h:127` | – | 확인 필요 |
| `RPiController::RgbySums` | `src/ipa/rpi/controller/statistics.h:18` | – | 확인 필요 |
| `RPiController::Saturation` | `src/ipa/rpi/controller/rpi/saturation.h:19` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::SaturationConfig` | `src/ipa/rpi/controller/rpi/saturation.h:13` | – | 확인 필요 |
| `RPiController::Sdn` | `src/ipa/rpi/controller/rpi/sdn.h:16` | `RPiController::DenoiseAlgorithm` | Algorithm to calculate correct spatial denoise (SDN) settings. |
| `RPiController::Sharpen` | `src/ipa/rpi/controller/rpi/sharpen.h:16` | `RPiController::SharpenAlgorithm` | 확인 필요 |
| `RPiController::SharpenAlgorithm` | `src/ipa/rpi/controller/sharpen_algorithm.h:13` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::Statistics` | `src/ipa/rpi/controller/statistics.h:32` | – | 확인 필요 |
| `RPiController::Statistics::AgcStatsPos` | `src/ipa/rpi/controller/statistics.h:44` | – | Positioning of the AGC statistics gathering in the pipeline: Pre-WB correction or post-WB correction. Assume this is post-LSC. |
| `RPiController::Statistics::ColourStatsPos` | `src/ipa/rpi/controller/statistics.h:51` | – | Positioning of the AWB/ALSC statistics gathering in the pipeline: Pre-LSC or post-LSC. |
| `RPiController::Tonemap` | `src/ipa/rpi/controller/rpi/tonemap.h:23` | `RPiController::Algorithm` | 확인 필요 |
| `RPiController::TonemapConfig` | `src/ipa/rpi/controller/rpi/tonemap.h:15` | – | 확인 필요 |
| `SaturationStatus` | `src/ipa/rpi/controller/saturation_status.h:9` | – | 확인 필요 |
| `SdnStatus` | `src/ipa/rpi/controller/denoise_status.h:18` | – | 확인 필요 |
| `SharpenStatus` | `src/ipa/rpi/controller/sharpen_status.h:11` | – | The "sharpen" algorithm stores the strength to use. |
| `StitchStatus` | `src/ipa/rpi/controller/stitch_status.h:13` | – | Parameters for the stitch block. |
| `TdnStatus` | `src/ipa/rpi/controller/denoise_status.h:31` | – | 확인 필요 |
| `TonemapStatus` | `src/ipa/rpi/controller/tonemap_status.h:11` | – | 확인 필요 |
| `libcamera::ipa::RPi::IpaBase` | `src/ipa/rpi/common/ipa_base.h:32` | `libcamera::ipa::RPi::IPARPiInterface` | 확인 필요 |
| `libcamera::ipa::RPi::IpaBase::FlickerState` | `src/ipa/rpi/common/ipa_base.h:139` | – | The current state of flicker avoidance. |
| `libcamera::ipa::RPi::IpaPiSP` | `src/ipa/rpi/pisp/pisp.cpp:214` | `libcamera::ipa::RPi::IpaBase` | 확인 필요 |
| `libcamera::ipa::RPi::IpaVc4` | `src/ipa/rpi/vc4/vc4.cpp:40` | `libcamera::ipa::RPi::IpaBase` | 확인 필요 |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `Create` | – | `src/ipa/rpi/controller/rpi/cac.cpp:103` | Register algorithm with the system. |
| `RPiController::create` | – | `src/ipa/rpi/controller/rpi/awb_bayes.cpp:438` | Register algorithm with the system. |
| `RPiController::getAlgorithms` | `src/ipa/rpi/controller/algorithm.h:66` | `src/ipa/rpi/controller/algorithm.cpp:47` | 확인 필요 |
| `RPiController::operator*` | – | `src/ipa/rpi/controller/rpi/awb.h:171` | 확인 필요 |
| `RPiController::operator+` | – | `src/ipa/rpi/controller/rpi/awb.h:163` | 확인 필요 |
| `RPiController::operator-` | – | `src/ipa/rpi/controller/rpi/awb.h:167` | 확인 필요 |
| `addLuminanceG` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:795` | 확인 필요 |
| `addLuminanceRb` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:787` | 확인 필요 |
| `addLuminanceToTables` | `src/ipa/rpi/controller/rpi/alsc.cpp:200` | `src/ipa/rpi/controller/rpi/alsc.cpp:803` | 확인 필요 |
| `algorithms` | – | `src/ipa/rpi/controller/algorithm.cpp:39` | 확인 필요 |
| `applyCalTable` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:565` | 확인 필요 |
| `applyManualContrast` | – | `src/ipa/rpi/controller/rpi/contrast.cpp:143` | 확인 필요 |
| `applySaturation` | – | `src/ipa/rpi/controller/rpi/ccm.cpp:130` | 확인 필요 |
| `arrayToSet` | – | `src/ipa/rpi/controller/rpi/cac.cpp:30` | 확인 필요 |
| `averageGains` | – | `src/ipa/rpi/controller/rpi/hdr.cpp:295` | 확인 필요 |
| `calculateCcm` | – | `src/ipa/rpi/controller/rpi/ccm.cpp:114` | 확인 필요 |
| `calculateCrCb` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:547` | Calculate chrominance statistics (R/G and B/G) for each region. |
| `camHelpers` | – | `src/ipa/rpi/cam_helper/cam_helper.cpp:30` | 확인 필요 |
| `compareModes` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:247` | 확인 필요 |
| `compensateLambdasForCal` | `src/ipa/rpi/controller/rpi/alsc.cpp:197` | `src/ipa/rpi/controller/rpi/alsc.cpp:572` | 확인 필요 |
| `computeInitialY` | – | `src/ipa/rpi/controller/rpi/agc_channel.cpp:633` | 확인 필요 |
| `computeLambdaBottom` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:658` | In the compute_lambda_ functions, note that the matrix coefficients for the left/right neighbours are zero down the left/right edges, so we don't need need to test the i value to exclude them. |
| `computeLambdaBottomStart` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:664` | 확인 필요 |
| `computeLambdaInterior` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:669` | 확인 필요 |
| `computeLambdaTop` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:675` | 확인 필요 |
| `computeLambdaTopEnd` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:681` | 확인 필요 |
| `computeStretchCurve` | – | `src/ipa/rpi/controller/rpi/contrast.cpp:99` | 확인 필요 |
| `computeW` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:613` | Compute all weights. |
| `computeWeight` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:604` | Compute weight out of 1.0 which reflects how similar we wish to make the colours of these two regions. |
| `constraintComputeGain` | – | `src/ipa/rpi/controller/rpi/agc_channel.cpp:703` | 확인 필요 |
| `constructM` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:629` | Compute M, the large but sparse matrix such that M * lambdas = 0. |
| `copyStats` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:341` | 확인 필요 |
| `create` | – | `src/ipa/rpi/cam_helper/cam_helper_ov5647.cpp:91` | Register algorithm with the system. |
| `gaussSeidel2Sor` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:688` | Gauss-Seidel iteration with over-relaxation. |
| `generateLut` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:53` | 확인 필요 |
| `getCalTable` | `src/ipa/rpi/controller/rpi/alsc.cpp:193` | `src/ipa/rpi/controller/rpi/alsc.cpp:459` | 확인 필요 |
| `getCt` | `src/ipa/rpi/controller/rpi/alsc.cpp:192` | `src/ipa/rpi/controller/rpi/alsc.cpp:328` | 확인 필요 |
| `getDelayedChannelIndex` | – | `src/ipa/rpi/controller/rpi/agc.cpp:270` | 확인 필요 |
| `getLocked` | – | `src/ipa/rpi/controller/rpi/ccm.cpp:105` | 확인 필요 |
| `hardwareConfigMap` | – | `src/ipa/rpi/controller/controller.cpp:26` | 확인 필요 |
| `libcamera::clampField` | – | `src/ipa/rpi/pisp/pisp.cpp:60` | 확인 필요 |
| `libcamera::generateDecompandLut` | – | `src/ipa/rpi/pisp/pisp.cpp:112` | 확인 필요 |
| `libcamera::generateLut` | – | `src/ipa/rpi/pisp/pisp.cpp:77` | 확인 필요 |
| `libcamera::logCategoryIPARPI` | `src/ipa/rpi/cam_helper/cam_helper.cpp:25` | – | 확인 필요 |
| `libcamera::packLscLut` | – | `src/ipa/rpi/pisp/pisp.cpp:131` | 확인 필요 |
| `libcamera::resampleTable` | – | `src/ipa/rpi/pisp/pisp.cpp:170` | Resamples a srcW x srcH table with central sampling to destW x destH with corner sampling. |
| `logCategoryRPiAf` | `src/ipa/rpi/controller/rpi/af.cpp:21` | – | 확인 필요 |
| `logCategoryRPiAgc` | `src/ipa/rpi/controller/rpi/agc.cpp:19` | – | 확인 필요 |
| `logCategoryRPiAlsc` | `src/ipa/rpi/controller/rpi/alsc.cpp:25` | – | 확인 필요 |
| `logCategoryRPiAwb` | `src/ipa/rpi/controller/rpi/awb.cpp:16` | – | 확인 필요 |
| `logCategoryRPiBlackLevel` | `src/ipa/rpi/controller/rpi/black_level.cpp:19` | – | 확인 필요 |
| `logCategoryRPiCac` | `src/ipa/rpi/controller/rpi/cac.cpp:16` | – | 확인 필요 |
| `logCategoryRPiCcm` | `src/ipa/rpi/controller/rpi/ccm.cpp:20` | – | 확인 필요 |
| `logCategoryRPiContrast` | `src/ipa/rpi/controller/rpi/contrast.cpp:19` | – | 확인 필요 |
| `logCategoryRPiController` | `src/ipa/rpi/controller/controller.cpp:22` | – | 확인 필요 |
| `logCategoryRPiDecompand` | `src/ipa/rpi/controller/rpi/decompand.cpp:13` | – | 확인 필요 |
| `logCategoryRPiDenoise` | `src/ipa/rpi/controller/rpi/denoise.cpp:17` | – | 확인 필요 |
| `logCategoryRPiDpc` | `src/ipa/rpi/controller/rpi/dpc.cpp:15` | – | 확인 필요 |
| `logCategoryRPiGeq` | `src/ipa/rpi/controller/rpi/geq.cpp:18` | – | 확인 필요 |
| `logCategoryRPiHdr` | `src/ipa/rpi/controller/rpi/hdr.cpp:22` | – | 확인 필요 |
| `logCategoryRPiLux` | `src/ipa/rpi/controller/rpi/lux.cpp:18` | – | 확인 필요 |
| `logCategoryRPiNoise` | `src/ipa/rpi/controller/rpi/noise.cpp:20` | – | 확인 필요 |
| `logCategoryRPiSaturation` | `src/ipa/rpi/controller/rpi/saturation.cpp:16` | – | 확인 필요 |
| `logCategoryRPiSdn` | `src/ipa/rpi/controller/rpi/sdn.cpp:19` | – | 확인 필요 |
| `logCategoryRPiSharpen` | `src/ipa/rpi/controller/rpi/sharpen.cpp:19` | – | 확인 필요 |
| `logCategoryRPiTonemap` | `src/ipa/rpi/controller/rpi/tonemap.cpp:16` | – | 확인 필요 |
| `normalise` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:742` | Normalise the values so that the smallest value is 1. |
| `operator<<` | – | `src/ipa/rpi/controller/device_status.cpp:11` | 확인 필요 |
| `printCalTable` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:585` | 확인 필요 |
| `readCalibrations` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:103` | 확인 필요 |
| `readChannelConstraints` | – | `src/ipa/rpi/controller/rpi/agc_channel.cpp:204` | 확인 필요 |
| `readConstraintMode` | – | `src/ipa/rpi/controller/rpi/agc_channel.cpp:140` | 확인 필요 |
| `readConstraintModes` | – | `src/ipa/rpi/controller/rpi/agc_channel.cpp:158` | 확인 필요 |
| `readCtCurve` | – | `src/ipa/rpi/controller/rpi/awb.cpp:20` | 확인 필요 |
| `readExposureModes` | – | `src/ipa/rpi/controller/rpi/agc_channel.cpp:94` | 확인 필요 |
| `readLut` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:85` | 확인 필요 |
| `readMeteringModes` | – | `src/ipa/rpi/controller/rpi/agc_channel.cpp:45` | 확인 필요 |
| `readNumber` | – | `src/ipa/rpi/controller/rpi/af.cpp:71` | 확인 필요 |
| `reaverage` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:750` | Rescale the values so that the average value is 1. |
| `resampleCalTable` | `src/ipa/rpi/controller/rpi/alsc.cpp:195` | `src/ipa/rpi/controller/rpi/alsc.cpp:489` | 확인 필요 |
| `runMatrixIterations` | – | `src/ipa/rpi/controller/rpi/alsc.cpp:758` | 확인 필요 |
| `setCurrentChannelIndexGetExposure` | – | `src/ipa/rpi/controller/rpi/agc.cpp:283` | 확인 필요 |
| `setStrength` | – | `src/ipa/rpi/controller/rpi/cac.cpp:45` | 확인 필요 |

## src/ipa/softisp

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::ipa::softisp::IPAActiveState` | `src/ipa/softisp/ipa_context.h:40` | – | The active state of the IPA algorithms |
| `libcamera::ipa::softisp::IPAActiveState::(unnamed struct at src/ipa/softisp/ipa_context.h:45:2)` | `src/ipa/softisp/ipa_context.h:45` | – | 확인 필요 |
| `libcamera::ipa::softisp::IPAActiveState::(unnamed struct at src/ipa/softisp/ipa_context.h:53:2)` | `src/ipa/softisp/ipa_context.h:53` | – | 확인 필요 |
| `libcamera::ipa::softisp::IPAContext` | `src/ipa/softisp/ipa_context.h:79` | – | Global IPA context data shared between all algorithms |
| `libcamera::ipa::softisp::IPAFrameContext` | `src/ipa/softisp/ipa_context.h:63` | `libcamera::ipa::FrameContext` | 확인 필요 |
| `libcamera::ipa::softisp::IPAFrameContext::(unnamed struct at src/ipa/softisp/ipa_context.h:68:2)` | `src/ipa/softisp/ipa_context.h:68` | – | 확인 필요 |
| `libcamera::ipa::softisp::IPASessionConfiguration` | `src/ipa/softisp/ipa_context.h:33` | – | Session configuration for the IPA module |
| `libcamera::ipa::softisp::IPASessionConfiguration::(unnamed struct at src/ipa/softisp/ipa_context.h:35:2)` | `src/ipa/softisp/ipa_context.h:35` | – | 확인 필요 |
| `libcamera::ipa::softisp::IPASoftIsp` | `src/ipa/softisp/softisp.cpp:45` | `libcamera::ipa::softisp::IPASoftIspInterface`, `libcamera::ipa::softisp::Module` | 확인 필요 |
| `libcamera::ipa::softisp::algorithms::Adjust` | `src/ipa/softisp/algorithms/adjust.h:22` | `libcamera::ipa::softisp::Algorithm` | 확인 필요 |
| `libcamera::ipa::softisp::algorithms::Agc` | `src/ipa/softisp/algorithms/agc.h:18` | `libcamera::ipa::softisp::Algorithm` | 확인 필요 |
| `libcamera::ipa::softisp::algorithms::AgcTraits` | `src/ipa/softisp/algorithms/agc.cpp:22` | `libcamera::ipa::AgcMeanLuminance::Traits` | 확인 필요 |
| `libcamera::ipa::softisp::algorithms::Awb` | `src/ipa/softisp/algorithms/awb.h:27` | `libcamera::ipa::softisp::Algorithm` | 확인 필요 |
| `libcamera::ipa::softisp::algorithms::BlackLevel` | `src/ipa/softisp/algorithms/blc.h:19` | `libcamera::ipa::softisp::Algorithm` | 확인 필요 |
| `libcamera::ipa::softisp::algorithms::Ccm` | `src/ipa/softisp/algorithms/ccm.h:24` | `libcamera::ipa::softisp::Algorithm` | 확인 필요 |
| `libcamera::ipa::softisp::algorithms::Lsc` | `src/ipa/softisp/algorithms/lsc.h:20` | `libcamera::ipa::softisp::Algorithm` | 확인 필요 |
| `libcamera::ipa::softisp::algorithms::SoftIspAwbStats` | `src/ipa/softisp/algorithms/awb.cpp:28` | `libcamera::ipa::AwbStats` | 확인 필요 |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::ipa::softisp::algorithms::logCategoryIPASoftIspAdjust` | `src/ipa/softisp/algorithms/adjust.cpp:25` | – | 확인 필요 |
| `libcamera::ipa::softisp::algorithms::logCategoryIPASoftIspBL` | `src/ipa/softisp/algorithms/blc.cpp:20` | – | 확인 필요 |
| `libcamera::ipa::softisp::algorithms::logCategoryIPASoftIspCcm` | `src/ipa/softisp/algorithms/ccm.cpp:17` | – | 확인 필요 |
| `libcamera::ipa::softisp::algorithms::logCategoryIPASoftIspLsc` | `src/ipa/softisp/algorithms/lsc.cpp:14` | – | 확인 필요 |
| `libcamera::logCategoryIPASoftIsp` | `src/ipa/softisp/softisp.cpp:36` | – | 확인 필요 |
| `libcamera::logCategoryIPASoftIspAwb` | `src/ipa/softisp/algorithms/awb.cpp:19` | – | 확인 필요 |
| `libcamera::logCategoryIPASoftIspExposure` | `src/ipa/softisp/algorithms/agc.cpp:16` | – | 확인 필요 |

## src/ipa/vimc

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::IPAVimc` | `src/ipa/vimc/vimc.cpp:29` | `libcamera::ipa::vimc::IPAVimcInterface` | 확인 필요 |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::logCategoryIPAVimc` | `src/ipa/vimc/vimc.cpp:27` | – | 확인 필요 |

## src/libcamera

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::BayerFormatComparator` | `src/libcamera/bayer_format.cpp:73` | – | Define a slightly arbitrary ordering so that we can use a std::map. |
| `libcamera::DmaBufAllocatorInfo` | `src/libcamera/dma_buf_allocator.cpp:37` | – | 확인 필요 |
| `libcamera::EnvironmentFixedProcessor` | `src/libcamera/global_configuration.cpp:44` | `libcamera::EnvironmentProcessor` | A processor that sets a fixed value. |
| `libcamera::EnvironmentListProcessor` | `src/libcamera/global_configuration.cpp:65` | `libcamera::EnvironmentProcessor` | A processor that parses the environment variable as a list of strings with a custom delimiter. |
| `libcamera::EnvironmentOverride` | `src/libcamera/global_configuration.cpp:93` | – | 확인 필요 |
| `libcamera::EnvironmentProcessor` | `src/libcamera/global_configuration.cpp:34` | – | 확인 필요 |
| `libcamera::EnvironmentValueProcessor` | `src/libcamera/global_configuration.cpp:84` | `libcamera::EnvironmentProcessor` | A processor that copies the value of the environment variable. |
| `libcamera::Formats` | `src/libcamera/bayer_format.cpp:93` | – | 확인 필요 |
| `libcamera::YamlParserContext` | `src/libcamera/yaml_parser.cpp:31` | – | Class for YamlParser parsing and context data |
| `libcamera::YamlParserContext::EventDeleter` | `src/libcamera/yaml_parser.cpp:41` | – | 확인 필요 |
| `libcamera::v4l2_subdev_routing_legacy` | `src/libcamera/v4l2_subdevice.cpp:1479` | – | Legacy routing support for pre-v6.10-rc1 kernels. Drop when v6.12-rc1 gets released. |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::closeAllFdsExcept` | – | `src/libcamera/process.cpp:41` | 확인 필요 |
| `libcamera::elfLoadSymbol` | – | `src/libcamera/ipa_module.cpp:107` | Retrieve address and size of a symbol from an mmap'ed ELF file |
| `libcamera::elfPointer` | – | `src/libcamera/ipa_module.cpp:44` | 확인 필요 |
| `libcamera::elfSection` | – | `src/libcamera/ipa_module.cpp:88` | 확인 필요 |
| `libcamera::elfVerifyIdent` | – | `src/libcamera/ipa_module.cpp:62` | 확인 필요 |
| `libcamera::fileDescriptorInode` | – | `src/libcamera/framebuffer.cpp:288` | 확인 필요 |
| `libcamera::ipaConfigurationFile` | – | `src/libcamera/ipa_proxy.cpp:33` | 확인 필요 |
| `libcamera::isLibcameraInstalled` | – | `src/libcamera/source_paths.cpp:40` | Check if libcamera is installed or not |
| `libcamera::logCategoryAllocator` | `src/libcamera/framebuffer_allocator.cpp:27` | – | 확인 필요 |
| `libcamera::logCategoryBuffer` | `src/libcamera/framebuffer.cpp:29` | – | 확인 필요 |
| `libcamera::logCategoryCamera` | `src/libcamera/camera.cpp:133` | – | 확인 필요 |
| `libcamera::logCategoryCameraLens` | `src/libcamera/camera_lens.cpp:21` | – | 확인 필요 |
| `libcamera::logCategoryClockRec` | `src/libcamera/clock_recovery.cpp:21` | – | 확인 필요 |
| `libcamera::logCategoryConfiguration` | `src/libcamera/global_configuration.cpp:129` | – | 확인 필요 |
| `libcamera::logCategoryControls` | `src/libcamera/controls.cpp:49` | – | 확인 필요 |
| `libcamera::logCategoryConverter` | `src/libcamera/converter.cpp:26` | – | 확인 필요 |
| `libcamera::logCategoryDebugControls` | `src/libcamera/debug_controls.cpp:14` | – | 확인 필요 |
| `libcamera::logCategoryDelayedControls` | `src/libcamera/delayed_controls.cpp:23` | – | 확인 필요 |
| `libcamera::logCategoryDeviceEnumerator` | `src/libcamera/device_enumerator.cpp:41` | – | 확인 필요 |
| `libcamera::logCategoryDmaBufAllocator` | `src/libcamera/dma_buf_allocator.cpp:54` | – | 확인 필요 |
| `libcamera::logCategoryFormats` | `src/libcamera/formats.cpp:24` | – | 확인 필요 |
| `libcamera::logCategoryIPAModule` | `src/libcamera/ipa_module.cpp:39` | – | 확인 필요 |
| `libcamera::logCategoryIPCPipe` | `src/libcamera/ipc_pipe.cpp:19` | – | 확인 필요 |
| `libcamera::logCategoryIPCUnixSocket` | `src/libcamera/ipc_unixsocket.cpp:27` | – | 확인 필요 |
| `libcamera::logCategoryMediaDevice` | `src/libcamera/media_device.cpp:33` | – | 확인 필요 |
| `libcamera::logCategoryMediaPipeline` | `src/libcamera/media_pipeline.cpp:35` | – | 확인 필요 |
| `libcamera::logCategoryPipeline` | `src/libcamera/pipeline_handler.cpp:47` | – | 확인 필요 |
| `libcamera::logCategoryProcess` | `src/libcamera/process.cpp:37` | – | 확인 필요 |
| `libcamera::logCategoryRequest` | `src/libcamera/request.cpp:39` | – | 확인 필요 |
| `libcamera::logCategorySerialization` | `src/libcamera/byte_stream_buffer.cpp:22` | – | 확인 필요 |
| `libcamera::logCategorySerializer` | `src/libcamera/control_serializer.cpp:32` | – | 확인 필요 |
| `libcamera::logCategoryStream` | `src/libcamera/stream.cpp:44` | – | 확인 필요 |
| `libcamera::logCategorySysFs` | `src/libcamera/sysfs.cpp:25` | – | 확인 필요 |
| `libcamera::logCategoryV4L2` | `src/libcamera/v4l2_device.cpp:36` | – | 확인 필요 |
| `libcamera::logCategoryValueNode` | `src/libcamera/value_node.cpp:27` | – | 확인 필요 |
| `libcamera::logCategoryYamlParser` | `src/libcamera/yaml_parser.cpp:27` | – | 확인 필요 |
| `libcamera::routeFromKernel` | – | `src/libcamera/v4l2_subdevice.cpp:1455` | 확인 필요 |
| `libcamera::routeToKernel` | – | `src/libcamera/v4l2_subdevice.cpp:1465` | 확인 필요 |
| `libcamera::routedSourcePads` | – | `src/libcamera/media_pipeline.cpp:100` | Retrieve all source pads connected to a sink pad through active routes |
| `libcamera::transformFromOrientation` | – | `src/libcamera/transform.cpp:307` | Return the transform representing orientation |

## src/libcamera/base

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::LogOutput` | `src/libcamera/base/log.cpp:109` | – | Log output |
| `libcamera::Logger` | `src/libcamera/base/log.cpp:298` | – | Message logger |
| `libcamera::MessageQueue` | `src/libcamera/base/thread.cpp:85` | – | A queue of posted messages |
| `libcamera::ThreadData` | `src/libcamera/base/thread.cpp:106` | – | Thread-local internal data |
| `libcamera::ThreadMain` | `src/libcamera/base/thread.cpp:144` | `libcamera::Thread` | Thread wrapper for the main thread |
| `libcamera::utils::Locale` | `src/libcamera/base/utils.cpp:497` | – | RAII wrapper around locale_t instances, to support global locale instances without leaking memory. |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::logCategoryEvent` | `src/libcamera/base/event_dispatcher.cpp:17` | – | 확인 필요 |
| `libcamera::logCategoryFile` | `src/libcamera/base/file.cpp:27` | – | 확인 필요 |
| `libcamera::logCategoryMessage` | `src/libcamera/base/message.cpp:33` | – | 확인 필요 |
| `libcamera::logCategoryObject` | `src/libcamera/base/object.cpp:26` | – | 확인 필요 |
| `libcamera::logCategorySharedFD` | `src/libcamera/base/shared_fd.cpp:25` | – | 확인 필요 |
| `libcamera::logCategoryThread` | `src/libcamera/base/thread.cpp:78` | – | 확인 필요 |
| `libcamera::logCategoryTimer` | `src/libcamera/base/timer.cpp:27` | – | 확인 필요 |
| `libcamera::logCategoryUniqueFD` | `src/libcamera/base/unique_fd.cpp:23` | – | 확인 필요 |
| `libcamera::log_severity_name` | – | `src/libcamera/base/log.cpp:88` | 확인 필요 |
| `libcamera::log_severity_to_syslog` | – | `src/libcamera/base/log.cpp:70` | 확인 필요 |
| `libcamera::notifierType` | – | `src/libcamera/base/event_dispatcher_poll.cpp:32` | 확인 필요 |

## src/libcamera/converter

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::dw100VerticesForLength` | – | `src/libcamera/converter/converter_dw100_vertexmap.cpp:153` | 확인 필요 |
| `libcamera::getCropBounds` | – | `src/libcamera/converter/converter_v4l2_m2m.cpp:41` | 확인 필요 |
| `libcamera::makeRotate` | – | `src/libcamera/converter/converter_dw100_vertexmap.cpp:49` | 확인 필요 |
| `libcamera::makeScale` | – | `src/libcamera/converter/converter_dw100_vertexmap.cpp:63` | 확인 필요 |
| `libcamera::makeTransform` | – | `src/libcamera/converter/converter_dw100_vertexmap.cpp:79` | \param t The transform to apply |
| `libcamera::makeTranslate` | – | `src/libcamera/converter/converter_dw100_vertexmap.cpp:36` | 확인 필요 |
| `libcamera::point2Vec2d` | – | `src/libcamera/converter/converter_dw100_vertexmap.cpp:148` | 확인 필요 |
| `libcamera::rotatedRectSize` | – | `src/libcamera/converter/converter_dw100_vertexmap.cpp:138` | 확인 필요 |
| `libcamera::transformPoint` | – | `src/libcamera/converter/converter_dw100_vertexmap.cpp:124` | 확인 필요 |
| `libcamera::transformVector` | – | `src/libcamera/converter/converter_dw100_vertexmap.cpp:131` | 확인 필요 |

## src/libcamera/pipeline

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::CIO2Device` | `src/libcamera/pipeline/ipu3/cio2.h:30` | – | 확인 필요 |
| `libcamera::Cfe` | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:50` | – | 확인 필요 |
| `libcamera::ColorBarsGenerator` | `src/libcamera/pipeline/virtual/test_pattern_generator.h:34` | `libcamera::TestPatternGenerator` | 확인 필요 |
| `libcamera::ConfigParser` | `src/libcamera/pipeline/virtual/config_parser.h:22` | – | 확인 필요 |
| `libcamera::DiagonalLinesGenerator` | `src/libcamera/pipeline/virtual/test_pattern_generator.h:41` | `libcamera::TestPatternGenerator` | 확인 필요 |
| `libcamera::FOV` | `src/libcamera/pipeline/ipu3/imgu.cpp:58` | – | 확인 필요 |
| `libcamera::FrameGenerator` | `src/libcamera/pipeline/virtual/frame_generator.h:16` | – | 확인 필요 |
| `libcamera::IPU3CameraConfiguration` | `src/libcamera/pipeline/ipu3/ipu3.cpp:96` | `libcamera::CameraConfiguration` | 확인 필요 |
| `libcamera::IPU3CameraData` | `src/libcamera/pipeline/ipu3/ipu3.cpp:50` | `libcamera::Camera::Private` | 확인 필요 |
| `libcamera::IPU3Frames` | `src/libcamera/pipeline/ipu3/frames.h:24` | – | 확인 필요 |
| `libcamera::IPU3Frames::Info` | `src/libcamera/pipeline/ipu3/frames.h:27` | – | 확인 필요 |
| `libcamera::ISICameraConfiguration` | `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp:79` | `libcamera::CameraConfiguration` | 확인 필요 |
| `libcamera::ISICameraData` | `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp:42` | `libcamera::Camera::Private` | 확인 필요 |
| `libcamera::ImageFrameGenerator` | `src/libcamera/pipeline/virtual/image_frame_generator.h:25` | `libcamera::FrameGenerator` | 확인 필요 |
| `libcamera::ImageFrameGenerator::ImageFrameData` | `src/libcamera/pipeline/virtual/image_frame_generator.h:33` | – | 확인 필요 |
| `libcamera::ImageFrames` | `src/libcamera/pipeline/virtual/image_frame_generator.h:21` | – | Frame configuration provided by the config file |
| `libcamera::ImgUDevice` | `src/libcamera/pipeline/ipu3/imgu.h:23` | – | 확인 필요 |
| `libcamera::ImgUDevice::Pipe` | `src/libcamera/pipeline/ipu3/imgu.h:61` | – | Describe the ImgU requested configuration |
| `libcamera::ImgUDevice::PipeConfig` | `src/libcamera/pipeline/ipu3/imgu.h:49` | – | The ImgU pipe configuration parameters |
| `libcamera::Isp` | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:51` | – | 확인 필요 |
| `libcamera::MaliC55CameraConfiguration` | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:493` | `libcamera::CameraConfiguration` | 확인 필요 |
| `libcamera::MaliC55CameraData` | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:100` | `libcamera::Camera::Private` | 확인 필요 |
| `libcamera::MaliC55CameraData::Inline` | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:110` | – | 확인 필요 |
| `libcamera::MaliC55CameraData::Memory` | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:115` | – | 확인 필요 |
| `libcamera::MaliC55CameraData::Tpg` | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:103` | – | 확인 필요 |
| `libcamera::MaliC55FrameInfo` | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:89` | – | 확인 필요 |
| `libcamera::PiSPCameraData` | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:717` | `libcamera::RPi::CameraData` | 확인 필요 |
| `libcamera::PiSPCameraData::CfeJob` | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:829` | – | 확인 필요 |
| `libcamera::PiSPCameraData::Config` | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:784` | – | 확인 필요 |
| `libcamera::PipelineHandlerIPU3` | `src/libcamera/pipeline/ipu3/ipu3.cpp:124` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerIPU3::IPU3PipeModes` | `src/libcamera/pipeline/ipu3/ipu3.cpp:130` | – | 확인 필요 |
| `libcamera::PipelineHandlerISI` | `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp:102` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerISI::Pipe` | `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp:129` | – | 확인 필요 |
| `libcamera::PipelineHandlerMaliC55` | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:676` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerMaliC55::(unnamed enum at src/libcamera/pipeline/mali-c55/mali-c55.cpp:712:2)` | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:712` | – | 확인 필요 |
| `libcamera::PipelineHandlerMaliC55::MaliC55Pipe` | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:705` | – | 확인 필요 |
| `libcamera::PipelineHandlerPiSP` | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:852` | `libcamera::RPi::PipelineHandlerBase` | 확인 필요 |
| `libcamera::PipelineHandlerRkISP1` | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:185` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerUVC` | `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:81` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerVc4` | `src/libcamera/pipeline/rpi/vc4/vc4.cpp:141` | `libcamera::RPi::PipelineHandlerBase` | 확인 필요 |
| `libcamera::PipelineHandlerVimc` | `src/libcamera/pipeline/vimc/vimc.cpp:84` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerVirtual` | `src/libcamera/pipeline/virtual/virtual.cpp:81` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::RPi::BufferMask` | `src/libcamera/pipeline/rpi/common/rpi_stream.h:28` | – | 확인 필요 |
| `libcamera::RPi::BufferObject` | `src/libcamera/pipeline/rpi/common/rpi_stream.h:35` | – | 확인 필요 |
| `libcamera::RPi::CameraData` | `src/libcamera/pipeline/rpi/common/pipeline_base.h:47` | `libcamera::Camera::Private` | 확인 필요 |
| `libcamera::RPi::CameraData::Config` | `src/libcamera/pipeline/rpi/common/pipeline_base.h:167` | – | 확인 필요 |
| `libcamera::RPi::CameraData::CropParams` | `src/libcamera/pipeline/rpi/common/pipeline_base.h:138` | – | 확인 필요 |
| `libcamera::RPi::CameraData::ImmediateControlsEntry` | `src/libcamera/pipeline/rpi/common/pipeline_base.h:184` | – | 확인 필요 |
| `libcamera::RPi::CameraData::State` | `src/libcamera/pipeline/rpi/common/pipeline_base.h:125` | – | All the functions in this class are called from a single calling thread. So, we do not need to have any mutex to protect access to any of the variables below. |
| `libcamera::RPi::DelayedControls` | `src/libcamera/pipeline/rpi/common/delayed_controls.h:25` | – | Helper to deal with controls that take effect with a delay |
| `libcamera::RPi::DelayedControls::ControlParams` | `src/libcamera/pipeline/rpi/common/delayed_controls.h:28` | – | Parameters associated with controls handled by the \a DelayedControls |
| `libcamera::RPi::DelayedControls::Info` | `src/libcamera/pipeline/rpi/common/delayed_controls.h:44` | `libcamera::ControlValue` | 확인 필요 |
| `libcamera::RPi::DelayedControls::RingBuffer` | `src/libcamera/pipeline/rpi/common/delayed_controls.h:62` | – | 확인 필요 |
| `libcamera::RPi::Device` | `src/libcamera/pipeline/rpi/common/rpi_stream.h:191` | – | The following class is just a convenient (and typesafe) array of device streams indexed with an enum class. |
| `libcamera::RPi::PipelineHandlerBase` | `src/libcamera/pipeline/rpi/common/pipeline_base.h:203` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::RPi::RPiCameraConfiguration` | `src/libcamera/pipeline/rpi/common/pipeline_base.h:263` | `libcamera::CameraConfiguration` | 확인 필요 |
| `libcamera::RPi::RPiCameraConfiguration::StreamParams` | `src/libcamera/pipeline/rpi/common/pipeline_base.h:279` | – | 확인 필요 |
| `libcamera::RPi::Stream` | `src/libcamera/pipeline/rpi/common/rpi_stream.h:54` | `libcamera::Stream` | Device stream abstraction for either an internal or external stream. Used for both Unicam and the ISP. |
| `libcamera::RPi::Stream::StreamFlag` | `src/libcamera/pipeline/rpi/common/rpi_stream.h:57` | – | 확인 필요 |
| `libcamera::RZG2LCRU` | `src/libcamera/pipeline/mali-c55/rzg2l-cru.h:26` | – | 확인 필요 |
| `libcamera::RkISP1CameraConfiguration` | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:142` | `libcamera::CameraConfiguration` | 확인 필요 |
| `libcamera::RkISP1CameraData` | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:94` | `libcamera::Camera::Private` | 확인 필요 |
| `libcamera::RkISP1FrameInfo` | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:60` | – | 확인 필요 |
| `libcamera::RkISP1Frames` | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:73` | – | 확인 필요 |
| `libcamera::RkISP1MainPath` | `src/libcamera/pipeline/rkisp1/rkisp1_path.h:91` | `libcamera::RkISP1Path` | 확인 필요 |
| `libcamera::RkISP1Path` | `src/libcamera/pipeline/rkisp1/rkisp1_path.h:34` | – | 확인 필요 |
| `libcamera::RkISP1SelfPath` | `src/libcamera/pipeline/rkisp1/rkisp1_path.h:97` | `libcamera::RkISP1Path` | 확인 필요 |
| `libcamera::SimpleCameraConfiguration` | `src/libcamera/pipeline/simple/simple.cpp:377` | `libcamera::CameraConfiguration` | 확인 필요 |
| `libcamera::SimpleCameraData` | `src/libcamera/pipeline/simple/simple.cpp:278` | `libcamera::Camera::Private` | 확인 필요 |
| `libcamera::SimpleCameraData::Configuration` | `src/libcamera/pipeline/simple/simple.cpp:326` | – | 확인 필요 |
| `libcamera::SimpleCameraData::Entity` | `src/libcamera/pipeline/simple/simple.cpp:301` | – | 확인 필요 |
| `libcamera::SimpleCameraData::RequestOutputs` | `src/libcamera/pipeline/simple/simple.cpp:353` | – | 확인 필요 |
| `libcamera::SimpleFrameInfo` | `src/libcamera/pipeline/simple/simple.cpp:191` | – | 확인 필요 |
| `libcamera::SimpleFrames` | `src/libcamera/pipeline/simple/simple.cpp:203` | – | 확인 필요 |
| `libcamera::SimplePipelineHandler` | `src/libcamera/pipeline/simple/simple.cpp:409` | `libcamera::PipelineHandler` | ----------------------------------------------------------------------------- |
| `libcamera::SimplePipelineHandler::EntityData` | `src/libcamera/pipeline/simple/simple.cpp:438` | – | 확인 필요 |
| `libcamera::SimplePipelineInfo` | `src/libcamera/pipeline/simple/simple.cpp:241` | – | 확인 필요 |
| `libcamera::TestPattern` | `src/libcamera/pipeline/virtual/test_pattern_generator.h:19` | – | 확인 필요 |
| `libcamera::TestPatternGenerator` | `src/libcamera/pipeline/virtual/test_pattern_generator.h:24` | `libcamera::FrameGenerator` | 확인 필요 |
| `libcamera::UVCCameraConfiguration` | `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:70` | `libcamera::CameraConfiguration` | 확인 필요 |
| `libcamera::UVCCameraData` | `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:41` | `libcamera::Camera::Private` | 확인 필요 |
| `libcamera::Unicam` | `src/libcamera/pipeline/rpi/vc4/vc4.cpp:33` | – | 확인 필요 |
| `libcamera::Vc4CameraData` | `src/libcamera/pipeline/rpi/vc4/vc4.cpp:38` | `libcamera::RPi::CameraData` | 확인 필요 |
| `libcamera::Vc4CameraData::BayerFrame` | `src/libcamera/pipeline/rpi/vc4/vc4.cpp:128` | – | 확인 필요 |
| `libcamera::Vc4CameraData::Config` | `src/libcamera/pipeline/rpi/vc4/vc4.cpp:94` | – | 확인 필요 |
| `libcamera::VimcCameraConfiguration` | `src/libcamera/pipeline/vimc/vimc.cpp:73` | `libcamera::CameraConfiguration` | 확인 필요 |
| `libcamera::VimcCameraData` | `src/libcamera/pipeline/vimc/vimc.cpp:48` | `libcamera::Camera::Private` | 확인 필요 |
| `libcamera::VirtualCameraConfiguration` | `src/libcamera/pipeline/virtual/virtual.cpp:68` | `libcamera::CameraConfiguration` | 확인 필요 |
| `libcamera::VirtualCameraData` | `src/libcamera/pipeline/virtual/virtual.h:32` | `libcamera::Camera::Private`, `libcamera::Thread`, `libcamera::Object` | 확인 필요 |
| `libcamera::VirtualCameraData::Configuration` | `src/libcamera/pipeline/virtual/virtual.h:49` | – | The config file is parsed to the Configuration struct |
| `libcamera::VirtualCameraData::Resolution` | `src/libcamera/pipeline/virtual/virtual.h:39` | – | 확인 필요 |
| `libcamera::VirtualCameraData::StreamConfig` | `src/libcamera/pipeline/virtual/virtual.h:43` | – | 확인 필요 |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `isFormatRaw` | – | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:54` | 확인 필요 |
| `libcamera::adjustSize` | – | `src/libcamera/pipeline/simple/simple.cpp:1111` | 확인 필요 |
| `libcamera::bayerToMbusCode` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:87` | 확인 필요 |
| `libcamera::calcFOV` | – | `src/libcamera/pipeline/ipu3/imgu.cpp:257` | 확인 필요 |
| `libcamera::calculateBDS` | – | `src/libcamera/pipeline/ipu3/imgu.cpp:185` | 확인 필요 |
| `libcamera::calculateBDSHeight` | – | `src/libcamera/pipeline/ipu3/imgu.cpp:108` | 확인 필요 |
| `libcamera::calculateGDC` | – | `src/libcamera/pipeline/ipu3/imgu.cpp:225` | 확인 필요 |
| `libcamera::calculateSwDownscale` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:698` | Calculate the amount of software downscale required (which is a power of 2). |
| `libcamera::computeOptimalStride` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:240` | 확인 필요 |
| `libcamera::currentTimestamp` | – | `src/libcamera/pipeline/virtual/virtual.cpp:57` | 확인 필요 |
| `libcamera::dmabufSyncEnd` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:313` | 확인 필요 |
| `libcamera::dmabufSyncStart` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:301` | 확인 필요 |
| `libcamera::do14bitUnpack` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:400` | 확인 필요 |
| `libcamera::do16BitEndianSwap` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:378` | 확인 필요 |
| `libcamera::do32BitConversion` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:326` | 확인 필요 |
| `libcamera::downscaleInterleaved2Internal` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:565` | 확인 필요 |
| `libcamera::downscaleInterleaved3` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:425` | 확인 필요 |
| `libcamera::downscaleInterleaved4` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:449` | 확인 필요 |
| `libcamera::downscaleInterleavedUyvy` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:540` | 확인 필요 |
| `libcamera::downscaleInterleavedYuyv` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:515` | 확인 필요 |
| `libcamera::downscalePlanar420` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:493` | 확인 필요 |
| `libcamera::downscalePlanar422` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:504` | 확인 필요 |
| `libcamera::downscalePlaneInternal` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:474` | 확인 필요 |
| `libcamera::downscaleSemiPlanar420` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:586` | 확인 필요 |
| `libcamera::downscaleStreamBuffer` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:597` | 확인 필요 |
| `libcamera::findScaleFactor` | – | `src/libcamera/pipeline/ipu3/imgu.cpp:73` | Approximate a scaling factor sf to the closest one available in a range. |
| `libcamera::findValidColorSpace` | – | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:87` | 확인 필요 |
| `libcamera::getFormatAlignment` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:681` | Return the minimum number of pixels required to write out multiples of 16 bytes. |
| `libcamera::getLargestWidth` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:669` | Return largest width of any of these streams (or of the camera input). |
| `libcamera::isControlDelayed` | – | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:1557` | 확인 필요 |
| `libcamera::isMonoSensor` | – | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:73` | 확인 필요 |
| `libcamera::isRaw` | – | `src/libcamera/pipeline/simple/simple.cpp:270` | 확인 필요 |
| `libcamera::isSameRatio` | – | `src/libcamera/pipeline/ipu3/imgu.cpp:97` | 확인 필요 |
| `libcamera::logCategoryIPU3` | `src/libcamera/pipeline/ipu3/cio2.cpp:27` | – | 확인 필요 |
| `libcamera::logCategoryISI` | `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp:38` | – | 확인 필요 |
| `libcamera::logCategoryMaliC55` | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:64` | – | 확인 필요 |
| `libcamera::logCategoryRPI` | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:33` | – | 확인 필요 |
| `libcamera::logCategoryRPISTREAM` | `src/libcamera/pipeline/rpi/common/rpi_stream.cpp:17` | – | 확인 필요 |
| `libcamera::logCategoryRPiDelayedControls` | `src/libcamera/pipeline/rpi/common/delayed_controls.cpp:25` | – | 확인 필요 |
| `libcamera::logCategoryRZG2LCRU` | `src/libcamera/pipeline/mali-c55/rzg2l-cru.cpp:36` | – | 확인 필요 |
| `libcamera::logCategoryRkISP1` | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:55` | – | 확인 필요 |
| `libcamera::logCategorySimplePipeline` | `src/libcamera/pipeline/simple/simple.cpp:53` | – | 확인 필요 |
| `libcamera::logCategoryUVC` | `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:39` | – | 확인 필요 |
| `libcamera::logCategoryVIMC` | `src/libcamera/pipeline/vimc/vimc.cpp:46` | – | 확인 필요 |
| `libcamera::logCategoryVirtual` | `src/libcamera/pipeline/virtual/config_parser.cpp:25` | – | 확인 필요 |
| `libcamera::mbusCodeToPixelFormat` | – | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:48` | 확인 필요 |
| `libcamera::mbusCodeUnpacked16` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:100` | 확인 필요 |
| `libcamera::setupOutputClipping` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:269` | 확인 필요 |
| `libcamera::toPiSPBayerOrder` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:108` | 확인 필요 |
| `libcamera::toPiSPImageFormat` | – | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:129` | 확인 필요 |
| `libcamera::v4l2ToExposureMode` | – | `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:116` | 확인 필요 |
| `rotateLeft1Column` | – | `src/libcamera/pipeline/virtual/test_pattern_generator.cpp:24` | 확인 필요 |

## src/libcamera/sensor

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::CameraSensorLegacy` | `src/libcamera/sensor/camera_sensor_legacy.cpp:55` | `libcamera::CameraSensor`, `libcamera::Loggable` | A camera sensor based on V4L2 subdevices |
| `libcamera::CameraSensorRaw` | `src/libcamera/sensor/camera_sensor_raw.cpp:56` | `libcamera::CameraSensor`, `libcamera::Loggable` | A camera sensor based on V4L2 subdevices |
| `libcamera::CameraSensorRaw::(unnamed struct at src/libcamera/sensor/camera_sensor_raw.cpp:128:2)` | `src/libcamera/sensor/camera_sensor_raw.cpp:128` | – | 확인 필요 |
| `libcamera::CameraSensorRaw::Streams` | `src/libcamera/sensor/camera_sensor_raw.cpp:123` | – | 확인 필요 |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::logCategoryCameraSensor` | `src/libcamera/sensor/camera_sensor.cpp:24` | – | 확인 필요 |
| `libcamera::logCategoryCameraSensorProperties` | `src/libcamera/sensor/camera_sensor_properties.cpp:31` | – | 확인 필요 |

## src/libcamera/software_isp

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::Debayer` | `src/libcamera/software_isp/debayer.h:35` | `libcamera::Object` | Base debayering class |
| `libcamera::Debayer::DebayerInputConfig` | `src/libcamera/software_isp/debayer.h:65` | – | Structure describing the incoming Bayer parameters |
| `libcamera::Debayer::DebayerOutputConfig` | `src/libcamera/software_isp/debayer.h:72` | – | Structure describing the output frame configuration |
| `libcamera::DebayerCpu` | `src/libcamera/software_isp/debayer_cpu.h:32` | `libcamera::Debayer` | Class for debayering on the CPU |
| `libcamera::DebayerCpu::CcmColumn` | `src/libcamera/software_isp/debayer_cpu.h:134` | – | 확인 필요 |
| `libcamera::DebayerCpuThread` | `src/libcamera/software_isp/debayer_cpu.cpp:39` | `libcamera::Thread`, `libcamera::Object` | Class representing one CPU debayering thread |
| `libcamera::DebayerEGL` | `src/libcamera/software_isp/debayer_egl.h:40` | `libcamera::Debayer` | Class for debayering using an EGL Shader |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `libcamera::logCategoryBenchmark` | `src/libcamera/software_isp/benchmark.cpp:20` | – | 확인 필요 |
| `libcamera::logCategoryDebayer` | `src/libcamera/software_isp/debayer.h:33` | – | Base debayering class |
| `libcamera::logCategorySwStatsCpu` | `src/libcamera/software_isp/swstats_cpu.cpp:160` | – | The offset of x, applied to window_.x for bayer variants |
| `libcamera::timeDiff` | – | `src/libcamera/software_isp/benchmark.cpp:49` | 확인 필요 |

## src/v4l2

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `V4L2Camera` | `src/v4l2/v4l2_camera.h:23` | – | 확인 필요 |
| `V4L2Camera::Buffer` | `src/v4l2/v4l2_camera.h:26` | – | 확인 필요 |
| `V4L2CameraFile` | `src/v4l2/v4l2_camera_file.h:16` | – | 확인 필요 |
| `V4L2CameraProxy` | `src/v4l2/v4l2_camera_proxy.h:25` | – | 확인 필요 |
| `V4L2CompatManager` | `src/v4l2/v4l2_compat_manager.h:20` | – | 확인 필요 |
| `V4L2CompatManager::FileOperations` | `src/v4l2/v4l2_compat_manager.h:23` | – | 확인 필요 |

| 함수 | 선언 위치 | 정의 위치 | 설명 (주석) |
|---|---|---|---|
| `__open64_2` | – | `src/v4l2/v4l2_compat.cpp:105` | 확인 필요 |
| `__open_2` | – | `src/v4l2/v4l2_compat.cpp:99` | 확인 필요 |
| `__openat64_2` | – | `src/v4l2/v4l2_compat.cpp:117` | 확인 필요 |
| `__openat_2` | – | `src/v4l2/v4l2_compat.cpp:111` | 확인 필요 |
| `close` | – | `src/v4l2/v4l2_compat.cpp:130` | 확인 필요 |
| `dup` | – | `src/v4l2/v4l2_compat.cpp:125` | 확인 필요 |
| `get_symbol` | – | `src/v4l2/v4l2_compat_manager.cpp:36` | 확인 필요 |
| `ioctl` | – | `src/v4l2/v4l2_compat.cpp:159` | 확인 필요 |
| `logCategoryV4L2Compat` | `src/v4l2/v4l2_camera.cpp:19` | – | 확인 필요 |
| `mmap` | – | `src/v4l2/v4l2_compat.cpp:135` | 확인 필요 |
| `mmap64` | – | `src/v4l2/v4l2_compat.cpp:143` | 확인 필요 |
| `munmap` | – | `src/v4l2/v4l2_compat.cpp:151` | 확인 필요 |
| `needs_mode` | – | `src/v4l2/v4l2_compat.cpp:39` | Determine if the flags require a further mode arguments that needs to be parsed from va_args. |
| `open` | – | `src/v4l2/v4l2_compat.cpp:48` | 확인 필요 |
| `open64` | – | `src/v4l2/v4l2_compat.cpp:59` | 확인 필요 |
| `openat` | – | `src/v4l2/v4l2_compat.cpp:70` | 확인 필요 |
| `openat64` | – | `src/v4l2/v4l2_compat.cpp:80` | 확인 필요 |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실로 만든 구조 설명
    - 검증 범위: 클래스와 관계를 facts에서 구성합니다. 실행 동작을 검증하지 않습니다.
    - 근거 파일: `include/libcamera/base/backtrace.h`, `include/libcamera/base/bound_method.h`, `include/libcamera/base/class.h`, `include/libcamera/base/event_dispatcher.h`, `include/libcamera/base/event_dispatcher_poll.h`, `include/libcamera/base/event_notifier.h`, `include/libcamera/base/file.h`, `include/libcamera/base/flags.h`, `include/libcamera/base/log.h`, `include/libcamera/base/memfd.h`, `include/libcamera/base/message.h`, `include/libcamera/base/mutex.h`, `include/libcamera/base/object.h`, `include/libcamera/base/semaphore.h`, `include/libcamera/base/shared_fd.h`, `include/libcamera/base/signal.h`, `include/libcamera/base/thread.h`, `include/libcamera/base/timer.h`, `include/libcamera/base/unique_fd.h`, `include/libcamera/base/utils.h`, `include/libcamera/camera.h`, `include/libcamera/camera_manager.h`, `include/libcamera/color_space.h`, `include/libcamera/controls.h`, `include/libcamera/fence.h`, `include/libcamera/framebuffer.h`, `include/libcamera/framebuffer_allocator.h`, `include/libcamera/geometry.h`, `include/libcamera/internal/bayer_format.h`, `include/libcamera/internal/byte_stream_buffer.h`, `include/libcamera/internal/camera.h`, `include/libcamera/internal/camera_controls.h`, `include/libcamera/internal/camera_lens.h`, `include/libcamera/internal/camera_manager.h`, `include/libcamera/internal/camera_sensor.h`, `include/libcamera/internal/camera_sensor_properties.h`, `include/libcamera/internal/clock_recovery.h`, `include/libcamera/internal/control_serializer.h`, `include/libcamera/internal/control_validator.h`, `include/libcamera/internal/converter.h`, `include/libcamera/internal/converter/converter_dw100.h`, `include/libcamera/internal/converter/converter_dw100_vertexmap.h`, `include/libcamera/internal/converter/converter_v4l2_m2m.h`, `include/libcamera/internal/debug_controls.h`, `include/libcamera/internal/delayed_controls.h`, `include/libcamera/internal/device_enumerator.h`, `include/libcamera/internal/device_enumerator_sysfs.h`, `include/libcamera/internal/device_enumerator_udev.h`, `include/libcamera/internal/dma_buf_allocator.h`, `include/libcamera/internal/egl.h`, `include/libcamera/internal/formats.h`, `include/libcamera/internal/framebuffer.h`, `include/libcamera/internal/global_configuration.h`, `include/libcamera/internal/ipa_data_serializer.h`, `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/ipa_module.h`, `include/libcamera/internal/ipa_proxy.h`, `include/libcamera/internal/ipc_pipe.h`, `include/libcamera/internal/ipc_pipe_unixsocket.h`, `include/libcamera/internal/ipc_unixsocket.h`, `include/libcamera/internal/mapped_framebuffer.h`, `include/libcamera/internal/matrix.h`, `include/libcamera/internal/media_device.h`, `include/libcamera/internal/media_object.h`, `include/libcamera/internal/media_pipeline.h`, `include/libcamera/internal/pipeline_handler.h`, `include/libcamera/internal/process.h`, `include/libcamera/internal/pub_key.h`, `include/libcamera/internal/request.h`, `include/libcamera/internal/shared_mem_object.h`, `include/libcamera/internal/software_isp/benchmark.h`, `include/libcamera/internal/software_isp/debayer_params.h`, `include/libcamera/internal/software_isp/software_isp.h`, `include/libcamera/internal/software_isp/swisp_stats.h`, `include/libcamera/internal/software_isp/swstats_cpu.h`, `include/libcamera/internal/sysfs.h`, `include/libcamera/internal/v4l2_device.h`, `include/libcamera/internal/v4l2_pixelformat.h`, `include/libcamera/internal/v4l2_request.h`, `include/libcamera/internal/v4l2_subdevice.h`, `include/libcamera/internal/v4l2_videodevice.h`, `include/libcamera/internal/value_node.h`, `include/libcamera/internal/vector.h`, `include/libcamera/internal/yaml_parser.h`, `include/libcamera/ipa/ipa_controls.h`, `include/libcamera/ipa/ipa_interface.h`, `include/libcamera/ipa/ipa_module_info.h`, `include/libcamera/logging.h`, `include/libcamera/orientation.h`, `include/libcamera/pixel_format.h`, `include/libcamera/request.h`, `include/libcamera/stream.h`, `include/libcamera/transform.h`, `src/apps/cam/camera_session.h`, `src/apps/cam/capture_script.h`, `src/apps/cam/drm.h`, `src/apps/cam/file_sink.h`, `src/apps/cam/frame_sink.h`, `src/apps/cam/kms_sink.h`, `src/apps/cam/main.cpp`, `src/apps/cam/main.h`, `src/apps/common/event_loop.h`, `src/apps/common/image.h`, `src/apps/common/options.cpp`, `src/apps/common/options.h`, `src/apps/common/ppm_writer.h`, `src/apps/common/stream_options.h`, `src/apps/ipa-verify/main.cpp`, `src/apps/lc-compliance/environment.h`, `src/apps/lc-compliance/helpers/capture.h`, `src/apps/lc-compliance/main.cpp`, `src/apps/lc-compliance/test_base.h`, `src/apps/lc-compliance/tests/capture_test.cpp`, `src/gstreamer/gstlibcamera-controls.h`, `src/gstreamer/gstlibcamera-utils.cpp`, `src/gstreamer/gstlibcamera-utils.h`, `src/gstreamer/gstlibcamera.cpp`, `src/gstreamer/gstlibcameraallocator.cpp`, `src/gstreamer/gstlibcameraallocator.h`, `src/gstreamer/gstlibcamerapad.cpp`, `src/gstreamer/gstlibcamerapad.h`, `src/gstreamer/gstlibcamerapool.cpp`, `src/gstreamer/gstlibcamerapool.h`, `src/gstreamer/gstlibcameraprovider.cpp`, `src/gstreamer/gstlibcameraprovider.h`, `src/gstreamer/gstlibcamerasrc.cpp`, `src/gstreamer/gstlibcamerasrc.h`, `src/ipa/ipu3/algorithms/af.cpp`, `src/ipa/ipu3/algorithms/af.h`, `src/ipa/ipu3/algorithms/agc.cpp`, `src/ipa/ipu3/algorithms/agc.h`, `src/ipa/ipu3/algorithms/awb.cpp`, `src/ipa/ipu3/algorithms/awb.h`, `src/ipa/ipu3/algorithms/blc.h`, `src/ipa/ipu3/algorithms/ccm.cpp`, `src/ipa/ipu3/algorithms/ccm.h`, `src/ipa/ipu3/algorithms/lsc.cpp`, `src/ipa/ipu3/algorithms/lsc.h`, `src/ipa/ipu3/algorithms/tone_mapping.h`, `src/ipa/ipu3/ipa_context.h`, `src/ipa/ipu3/ipu3.cpp`, `src/ipa/libipa/agc.cpp`, `src/ipa/libipa/agc.h`, `src/ipa/libipa/agc_mean_luminance.cpp`, `src/ipa/libipa/agc_mean_luminance.h`, `src/ipa/libipa/agc_msv.cpp`, `src/ipa/libipa/agc_msv.h`, `src/ipa/libipa/algorithm.h`, `src/ipa/libipa/awb.h`, `src/ipa/libipa/awb_bayes.cpp`, `src/ipa/libipa/awb_bayes.h`, `src/ipa/libipa/awb_grey.h`, `src/ipa/libipa/camera_sensor_helper.cpp`, `src/ipa/libipa/camera_sensor_helper.h`, `src/ipa/libipa/ccm.cpp`, `src/ipa/libipa/ccm.h`, `src/ipa/libipa/colours.cpp`, `src/ipa/libipa/colours.h`, `src/ipa/libipa/exposure_mode_helper.cpp`, `src/ipa/libipa/exposure_mode_helper.h`, `src/ipa/libipa/fc_queue.h`, `src/ipa/libipa/fixedpoint.h`, `src/ipa/libipa/gamma.h`, `src/ipa/libipa/histogram.h`, `src/ipa/libipa/interpolator.h`, `src/ipa/libipa/lsc.cpp`, `src/ipa/libipa/lsc.h`, `src/ipa/libipa/lsc_base.h`, `src/ipa/libipa/lsc_polynomial.cpp`, `src/ipa/libipa/lsc_polynomial.h`, `src/ipa/libipa/lsc_table.h`, `src/ipa/libipa/lux.cpp`, `src/ipa/libipa/lux.h`, `src/ipa/libipa/module.h`, `src/ipa/libipa/pwl.h`, `src/ipa/libipa/quantized.h`, `src/ipa/libipa/v4l2_params.h`, `src/ipa/libipa/v4l2_stats.cpp`, `src/ipa/libipa/v4l2_stats.h`, `src/ipa/mali-c55/algorithms/agc.cpp`, `src/ipa/mali-c55/algorithms/agc.h`, `src/ipa/mali-c55/algorithms/algorithm.h`, `src/ipa/mali-c55/algorithms/awb.cpp`, `src/ipa/mali-c55/algorithms/awb.h`, `src/ipa/mali-c55/algorithms/blc.cpp`, `src/ipa/mali-c55/algorithms/blc.h`, `src/ipa/mali-c55/algorithms/ccm.cpp`, `src/ipa/mali-c55/algorithms/ccm.h`, `src/ipa/mali-c55/algorithms/lsc.cpp`, `src/ipa/mali-c55/algorithms/lsc.h`, `src/ipa/mali-c55/ipa_context.h`, `src/ipa/mali-c55/mali-c55.cpp`, `src/ipa/mali-c55/params.h`, `src/ipa/rkisp1/algorithms/agc.cpp`, `src/ipa/rkisp1/algorithms/agc.h`, `src/ipa/rkisp1/algorithms/algorithm.h`, `src/ipa/rkisp1/algorithms/awb.cpp`, `src/ipa/rkisp1/algorithms/awb.h`, `src/ipa/rkisp1/algorithms/blc.cpp`, `src/ipa/rkisp1/algorithms/blc.h`, `src/ipa/rkisp1/algorithms/ccm.cpp`, `src/ipa/rkisp1/algorithms/ccm.h`, `src/ipa/rkisp1/algorithms/compress.cpp`, `src/ipa/rkisp1/algorithms/compress.h`, `src/ipa/rkisp1/algorithms/cproc.cpp`, `src/ipa/rkisp1/algorithms/cproc.h`, `src/ipa/rkisp1/algorithms/dpcc.cpp`, `src/ipa/rkisp1/algorithms/dpcc.h`, `src/ipa/rkisp1/algorithms/dpf.cpp`, `src/ipa/rkisp1/algorithms/dpf.h`, `src/ipa/rkisp1/algorithms/filter.cpp`, `src/ipa/rkisp1/algorithms/filter.h`, `src/ipa/rkisp1/algorithms/goc.cpp`, `src/ipa/rkisp1/algorithms/goc.h`, `src/ipa/rkisp1/algorithms/gsl.cpp`, `src/ipa/rkisp1/algorithms/gsl.h`, `src/ipa/rkisp1/algorithms/lsc.cpp`, `src/ipa/rkisp1/algorithms/lsc.h`, `src/ipa/rkisp1/algorithms/lux.h`, `src/ipa/rkisp1/algorithms/wdr.cpp`, `src/ipa/rkisp1/algorithms/wdr.h`, `src/ipa/rkisp1/ipa_context.h`, `src/ipa/rkisp1/params.cpp`, `src/ipa/rkisp1/params.h`, `src/ipa/rkisp1/rkisp1.cpp`, `src/ipa/rpi/cam_helper/cam_helper.cpp`, `src/ipa/rpi/cam_helper/cam_helper.h`, `src/ipa/rpi/cam_helper/cam_helper_imx219.cpp`, `src/ipa/rpi/cam_helper/cam_helper_imx283.cpp`, `src/ipa/rpi/cam_helper/cam_helper_imx290.cpp`, `src/ipa/rpi/cam_helper/cam_helper_imx296.cpp`, `src/ipa/rpi/cam_helper/cam_helper_imx355.cpp`, `src/ipa/rpi/cam_helper/cam_helper_imx415.cpp`, `src/ipa/rpi/cam_helper/cam_helper_imx477.cpp`, `src/ipa/rpi/cam_helper/cam_helper_imx519.cpp`, `src/ipa/rpi/cam_helper/cam_helper_imx708.cpp`, `src/ipa/rpi/cam_helper/cam_helper_mira220.cpp`, `src/ipa/rpi/cam_helper/cam_helper_ov5647.cpp`, `src/ipa/rpi/cam_helper/cam_helper_ov64a40.cpp`, `src/ipa/rpi/cam_helper/cam_helper_ov7251.cpp`, `src/ipa/rpi/cam_helper/cam_helper_ov9281.cpp`, `src/ipa/rpi/cam_helper/cam_helper_starvis2.cpp`, `src/ipa/rpi/cam_helper/cam_helper_vd55g1.cpp`, `src/ipa/rpi/cam_helper/cam_helper_vd56g3.cpp`, `src/ipa/rpi/cam_helper/md_parser.h`, `src/ipa/rpi/common/ipa_base.h`, `src/ipa/rpi/controller/af_algorithm.h`, `src/ipa/rpi/controller/af_status.h`, `src/ipa/rpi/controller/agc_algorithm.h`, `src/ipa/rpi/controller/agc_status.h`, `src/ipa/rpi/controller/algorithm.cpp`, `src/ipa/rpi/controller/algorithm.h`, `src/ipa/rpi/controller/alsc_status.h`, `src/ipa/rpi/controller/awb_algorithm.h`, `src/ipa/rpi/controller/awb_status.h`, `src/ipa/rpi/controller/black_level_algorithm.h`, `src/ipa/rpi/controller/black_level_status.h`, `src/ipa/rpi/controller/cac_status.h`, `src/ipa/rpi/controller/camera_mode.h`, `src/ipa/rpi/controller/ccm_algorithm.h`, `src/ipa/rpi/controller/ccm_status.h`, `src/ipa/rpi/controller/contrast_algorithm.h`, `src/ipa/rpi/controller/contrast_status.h`, `src/ipa/rpi/controller/controller.cpp`, `src/ipa/rpi/controller/controller.h`, `src/ipa/rpi/controller/decompand_algorithm.h`, `src/ipa/rpi/controller/decompand_status.h`, `src/ipa/rpi/controller/denoise_algorithm.h`, `src/ipa/rpi/controller/denoise_status.h`, `src/ipa/rpi/controller/device_status.cpp`, `src/ipa/rpi/controller/device_status.h`, `src/ipa/rpi/controller/dpc_status.h`, `src/ipa/rpi/controller/geq_status.h`, `src/ipa/rpi/controller/hdr_algorithm.h`, `src/ipa/rpi/controller/hdr_status.h`, `src/ipa/rpi/controller/histogram.h`, `src/ipa/rpi/controller/lux_status.h`, `src/ipa/rpi/controller/metadata.h`, `src/ipa/rpi/controller/noise_status.h`, `src/ipa/rpi/controller/pdaf_data.h`, `src/ipa/rpi/controller/region_stats.h`, `src/ipa/rpi/controller/rpi/af.cpp`, `src/ipa/rpi/controller/rpi/af.h`, `src/ipa/rpi/controller/rpi/agc.cpp`, `src/ipa/rpi/controller/rpi/agc.h`, `src/ipa/rpi/controller/rpi/agc_channel.cpp`, `src/ipa/rpi/controller/rpi/agc_channel.h`, `src/ipa/rpi/controller/rpi/alsc.cpp`, `src/ipa/rpi/controller/rpi/alsc.h`, `src/ipa/rpi/controller/rpi/awb.cpp`, `src/ipa/rpi/controller/rpi/awb.h`, `src/ipa/rpi/controller/rpi/awb_bayes.cpp`, `src/ipa/rpi/controller/rpi/black_level.cpp`, `src/ipa/rpi/controller/rpi/black_level.h`, `src/ipa/rpi/controller/rpi/cac.cpp`, `src/ipa/rpi/controller/rpi/cac.h`, `src/ipa/rpi/controller/rpi/ccm.cpp`, `src/ipa/rpi/controller/rpi/ccm.h`, `src/ipa/rpi/controller/rpi/contrast.cpp`, `src/ipa/rpi/controller/rpi/contrast.h`, `src/ipa/rpi/controller/rpi/decompand.cpp`, `src/ipa/rpi/controller/rpi/decompand.h`, `src/ipa/rpi/controller/rpi/denoise.cpp`, `src/ipa/rpi/controller/rpi/denoise.h`, `src/ipa/rpi/controller/rpi/dpc.cpp`, `src/ipa/rpi/controller/rpi/dpc.h`, `src/ipa/rpi/controller/rpi/geq.cpp`, `src/ipa/rpi/controller/rpi/geq.h`, `src/ipa/rpi/controller/rpi/hdr.cpp`, `src/ipa/rpi/controller/rpi/hdr.h`, `src/ipa/rpi/controller/rpi/lux.cpp`, `src/ipa/rpi/controller/rpi/lux.h`, `src/ipa/rpi/controller/rpi/noise.cpp`, `src/ipa/rpi/controller/rpi/noise.h`, `src/ipa/rpi/controller/rpi/saturation.cpp`, `src/ipa/rpi/controller/rpi/saturation.h`, `src/ipa/rpi/controller/rpi/sdn.cpp`, `src/ipa/rpi/controller/rpi/sdn.h`, `src/ipa/rpi/controller/rpi/sharpen.cpp`, `src/ipa/rpi/controller/rpi/sharpen.h`, `src/ipa/rpi/controller/rpi/tonemap.cpp`, `src/ipa/rpi/controller/rpi/tonemap.h`, `src/ipa/rpi/controller/saturation_status.h`, `src/ipa/rpi/controller/sharpen_algorithm.h`, `src/ipa/rpi/controller/sharpen_status.h`, `src/ipa/rpi/controller/statistics.h`, `src/ipa/rpi/controller/stitch_status.h`, `src/ipa/rpi/controller/tonemap_status.h`, `src/ipa/rpi/pisp/pisp.cpp`, `src/ipa/rpi/vc4/vc4.cpp`, `src/ipa/softisp/algorithms/adjust.cpp`, `src/ipa/softisp/algorithms/adjust.h`, `src/ipa/softisp/algorithms/agc.cpp`, `src/ipa/softisp/algorithms/agc.h`, `src/ipa/softisp/algorithms/awb.cpp`, `src/ipa/softisp/algorithms/awb.h`, `src/ipa/softisp/algorithms/blc.cpp`, `src/ipa/softisp/algorithms/blc.h`, `src/ipa/softisp/algorithms/ccm.cpp`, `src/ipa/softisp/algorithms/ccm.h`, `src/ipa/softisp/algorithms/lsc.cpp`, `src/ipa/softisp/algorithms/lsc.h`, `src/ipa/softisp/ipa_context.h`, `src/ipa/softisp/softisp.cpp`, `src/ipa/vimc/vimc.cpp`, `src/libcamera/base/event_dispatcher.cpp`, `src/libcamera/base/event_dispatcher_poll.cpp`, `src/libcamera/base/file.cpp`, `src/libcamera/base/log.cpp`, `src/libcamera/base/message.cpp`, `src/libcamera/base/object.cpp`, `src/libcamera/base/shared_fd.cpp`, `src/libcamera/base/thread.cpp`, `src/libcamera/base/timer.cpp`, `src/libcamera/base/unique_fd.cpp`, `src/libcamera/base/utils.cpp`, `src/libcamera/bayer_format.cpp`, `src/libcamera/byte_stream_buffer.cpp`, `src/libcamera/camera.cpp`, `src/libcamera/camera_lens.cpp`, `src/libcamera/clock_recovery.cpp`, `src/libcamera/control_serializer.cpp`, `src/libcamera/controls.cpp`, `src/libcamera/converter.cpp`, `src/libcamera/converter/converter_dw100_vertexmap.cpp`, `src/libcamera/converter/converter_v4l2_m2m.cpp`, `src/libcamera/debug_controls.cpp`, `src/libcamera/delayed_controls.cpp`, `src/libcamera/device_enumerator.cpp`, `src/libcamera/dma_buf_allocator.cpp`, `src/libcamera/formats.cpp`, `src/libcamera/framebuffer.cpp`, `src/libcamera/framebuffer_allocator.cpp`, `src/libcamera/geometry.cpp`, `src/libcamera/global_configuration.cpp`, `src/libcamera/ipa_module.cpp`, `src/libcamera/ipa_proxy.cpp`, `src/libcamera/ipc_pipe.cpp`, `src/libcamera/ipc_unixsocket.cpp`, `src/libcamera/matrix.cpp`, `src/libcamera/media_device.cpp`, `src/libcamera/media_pipeline.cpp`, `src/libcamera/orientation.cpp`, `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp`, `src/libcamera/pipeline/ipu3/cio2.cpp`, `src/libcamera/pipeline/ipu3/cio2.h`, `src/libcamera/pipeline/ipu3/frames.h`, `src/libcamera/pipeline/ipu3/imgu.cpp`, `src/libcamera/pipeline/ipu3/imgu.h`, `src/libcamera/pipeline/ipu3/ipu3.cpp`, `src/libcamera/pipeline/mali-c55/mali-c55.cpp`, `src/libcamera/pipeline/mali-c55/rzg2l-cru.cpp`, `src/libcamera/pipeline/mali-c55/rzg2l-cru.h`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1_path.h`, `src/libcamera/pipeline/rpi/common/delayed_controls.cpp`, `src/libcamera/pipeline/rpi/common/delayed_controls.h`, `src/libcamera/pipeline/rpi/common/pipeline_base.cpp`, `src/libcamera/pipeline/rpi/common/pipeline_base.h`, `src/libcamera/pipeline/rpi/common/rpi_stream.cpp`, `src/libcamera/pipeline/rpi/common/rpi_stream.h`, `src/libcamera/pipeline/rpi/pisp/pisp.cpp`, `src/libcamera/pipeline/rpi/vc4/vc4.cpp`, `src/libcamera/pipeline/simple/simple.cpp`, `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp`, `src/libcamera/pipeline/vimc/vimc.cpp`, `src/libcamera/pipeline/virtual/config_parser.cpp`, `src/libcamera/pipeline/virtual/config_parser.h`, `src/libcamera/pipeline/virtual/frame_generator.h`, `src/libcamera/pipeline/virtual/image_frame_generator.h`, `src/libcamera/pipeline/virtual/test_pattern_generator.cpp`, `src/libcamera/pipeline/virtual/test_pattern_generator.h`, `src/libcamera/pipeline/virtual/virtual.cpp`, `src/libcamera/pipeline/virtual/virtual.h`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/process.cpp`, `src/libcamera/request.cpp`, `src/libcamera/sensor/camera_sensor.cpp`, `src/libcamera/sensor/camera_sensor_legacy.cpp`, `src/libcamera/sensor/camera_sensor_properties.cpp`, `src/libcamera/sensor/camera_sensor_raw.cpp`, `src/libcamera/software_isp/benchmark.cpp`, `src/libcamera/software_isp/debayer.h`, `src/libcamera/software_isp/debayer_cpu.cpp`, `src/libcamera/software_isp/debayer_cpu.h`, `src/libcamera/software_isp/debayer_egl.h`, `src/libcamera/software_isp/swstats_cpu.cpp`, `src/libcamera/source_paths.cpp`, `src/libcamera/stream.cpp`, `src/libcamera/sysfs.cpp`, `src/libcamera/transform.cpp`, `src/libcamera/v4l2_device.cpp`, `src/libcamera/v4l2_subdevice.cpp`, `src/libcamera/value_node.cpp`, `src/libcamera/vector.cpp`, `src/libcamera/yaml_parser.cpp`, `src/v4l2/v4l2_camera.cpp`, `src/v4l2/v4l2_camera.h`, `src/v4l2/v4l2_camera_file.h`, `src/v4l2/v4l2_camera_proxy.h`, `src/v4l2/v4l2_compat.cpp`, `src/v4l2/v4l2_compat_manager.cpp`, `src/v4l2/v4l2_compat_manager.h`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `960713a8f9`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-26 · 사람 검토 전

다음 단계: [시스템 개요](overview.md)
