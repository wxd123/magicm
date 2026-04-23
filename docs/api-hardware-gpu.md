# `gpu`

## Table of Contents

- 🅼 [gpu](#gpu)
- 🅼 [gpu\.amd](#gpu-amd)
- 🅼 [gpu\.commands](#gpu-commands)
- 🅼 [gpu\.commands\.amd\_command](#gpu-commands-amd_command)
- 🅼 [gpu\.commands\.apple\_command](#gpu-commands-apple_command)
- 🅼 [gpu\.commands\.huawei\_command](#gpu-commands-huawei_command)
- 🅼 [gpu\.commands\.intel\_command](#gpu-commands-intel_command)
- 🅼 [gpu\.commands\.nvidia\_command](#gpu-commands-nvidia_command)
- 🅼 [gpu\.commands\.qualcomm\_command](#gpu-commands-qualcomm_command)
- 🅼 [gpu\.core](#gpu-core)
- 🅼 [gpu\.core\.base](#gpu-core-base)
- 🅼 [gpu\.core\.command\_executor](#gpu-core-command_executor)
- 🅼 [gpu\.core\.factory](#gpu-core-factory)
- 🅼 [gpu\.gpu\_detector](#gpu-gpu_detector)
- 🅼 [gpu\.vendor](#gpu-vendor)
- 🅼 [gpu\.vendor\.amd](#gpu-vendor-amd)
- 🅼 [gpu\.vendor\.huawei](#gpu-vendor-huawei)
- 🅼 [gpu\.vendor\.intel](#gpu-vendor-intel)
- 🅼 [gpu\.vendor\.nvidia](#gpu-vendor-nvidia)
- 🅼 [gpu\.vendor\.utils](#gpu-vendor-utils)

<a name="gpu"></a>
## 🅼 gpu
<a name="gpu-amd"></a>
## 🅼 gpu\.amd
<a name="gpu-commands"></a>
## 🅼 gpu\.commands

- **[Exports](#gpu-commands-exports)**

<a name="gpu-commands-exports"></a>
### Exports

- 🅼 [`NVIDIACommand`](#gpu-commands-NVIDIACommand)
- 🅼 [`AMDCommand`](#gpu-commands-AMDCommand)
- 🅼 [`IntelCommand`](#gpu-commands-IntelCommand)
- 🅼 [`HuaweiCommand`](#gpu-commands-HuaweiCommand)
<a name="gpu-commands-amd_command"></a>
## 🅼 gpu\.commands\.amd\_command

- **Classes:**
  - 🅲 [AMDCommand](#gpu-commands-amd_command-AMDCommand)

### Classes

<a name="gpu-commands-amd_command-AMDCommand"></a>
### 🅲 gpu\.commands\.amd\_command\.AMDCommand

```python
class AMDCommand(GPUDetectionCommand):
```

AMD GPU检测命令

**Functions:**

<a name="gpu-commands-amd_command-AMDCommand-get_vendor"></a>
#### 🅵 gpu\.commands\.amd\_command\.AMDCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="gpu-commands-amd_command-AMDCommand-get_priority"></a>
#### 🅵 gpu\.commands\.amd\_command\.AMDCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="gpu-commands-amd_command-AMDCommand-execute"></a>
#### 🅵 gpu\.commands\.amd\_command\.AMDCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行AMD GPU检测
<a name="gpu-commands-apple_command"></a>
## 🅼 gpu\.commands\.apple\_command

- **Classes:**
  - 🅲 [AppleCommand](#gpu-commands-apple_command-AppleCommand)

### Classes

<a name="gpu-commands-apple_command-AppleCommand"></a>
### 🅲 gpu\.commands\.apple\_command\.AppleCommand

```python
class AppleCommand(GPUDetectionCommand):
```

Apple Silicon GPU检测命令 - 新增厂商示例

**Functions:**

<a name="gpu-commands-apple_command-AppleCommand-get_vendor"></a>
#### 🅵 gpu\.commands\.apple\_command\.AppleCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="gpu-commands-apple_command-AppleCommand-get_priority"></a>
#### 🅵 gpu\.commands\.apple\_command\.AppleCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="gpu-commands-apple_command-AppleCommand-execute"></a>
#### 🅵 gpu\.commands\.apple\_command\.AppleCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行Apple Silicon GPU检测
<a name="gpu-commands-huawei_command"></a>
## 🅼 gpu\.commands\.huawei\_command

- **Classes:**
  - 🅲 [HuaweiCommand](#gpu-commands-huawei_command-HuaweiCommand)

### Classes

<a name="gpu-commands-huawei_command-HuaweiCommand"></a>
### 🅲 gpu\.commands\.huawei\_command\.HuaweiCommand

```python
class HuaweiCommand(GPUDetectionCommand):
```

华为昇腾GPU检测命令

**Functions:**

<a name="gpu-commands-huawei_command-HuaweiCommand-get_vendor"></a>
#### 🅵 gpu\.commands\.huawei\_command\.HuaweiCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="gpu-commands-huawei_command-HuaweiCommand-get_priority"></a>
#### 🅵 gpu\.commands\.huawei\_command\.HuaweiCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="gpu-commands-huawei_command-HuaweiCommand-execute"></a>
#### 🅵 gpu\.commands\.huawei\_command\.HuaweiCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行华为昇腾GPU检测
<a name="gpu-commands-intel_command"></a>
## 🅼 gpu\.commands\.intel\_command

- **Classes:**
  - 🅲 [IntelCommand](#gpu-commands-intel_command-IntelCommand)

### Classes

<a name="gpu-commands-intel_command-IntelCommand"></a>
### 🅲 gpu\.commands\.intel\_command\.IntelCommand

```python
class IntelCommand(GPUDetectionCommand):
```

Intel GPU检测命令

**Functions:**

<a name="gpu-commands-intel_command-IntelCommand-get_vendor"></a>
#### 🅵 gpu\.commands\.intel\_command\.IntelCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="gpu-commands-intel_command-IntelCommand-get_priority"></a>
#### 🅵 gpu\.commands\.intel\_command\.IntelCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="gpu-commands-intel_command-IntelCommand-execute"></a>
#### 🅵 gpu\.commands\.intel\_command\.IntelCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行Intel GPU检测
<a name="gpu-commands-nvidia_command"></a>
## 🅼 gpu\.commands\.nvidia\_command

- **Classes:**
  - 🅲 [NVIDIACommand](#gpu-commands-nvidia_command-NVIDIACommand)

### Classes

<a name="gpu-commands-nvidia_command-NVIDIACommand"></a>
### 🅲 gpu\.commands\.nvidia\_command\.NVIDIACommand

```python
class NVIDIACommand(GPUDetectionCommand):
```

NVIDIA GPU检测命令

**Functions:**

<a name="gpu-commands-nvidia_command-NVIDIACommand-get_vendor"></a>
#### 🅵 gpu\.commands\.nvidia\_command\.NVIDIACommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="gpu-commands-nvidia_command-NVIDIACommand-get_priority"></a>
#### 🅵 gpu\.commands\.nvidia\_command\.NVIDIACommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="gpu-commands-nvidia_command-NVIDIACommand-execute"></a>
#### 🅵 gpu\.commands\.nvidia\_command\.NVIDIACommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行NVIDIA GPU检测
<a name="gpu-commands-qualcomm_command"></a>
## 🅼 gpu\.commands\.qualcomm\_command

- **Classes:**
  - 🅲 [QualcommCommand](#gpu-commands-qualcomm_command-QualcommCommand)

### Classes

<a name="gpu-commands-qualcomm_command-QualcommCommand"></a>
### 🅲 gpu\.commands\.qualcomm\_command\.QualcommCommand

```python
class QualcommCommand(GPUDetectionCommand):
```

高通Adreno GPU检测命令 - 新增厂商示例

**Functions:**

<a name="gpu-commands-qualcomm_command-QualcommCommand-get_vendor"></a>
#### 🅵 gpu\.commands\.qualcomm\_command\.QualcommCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="gpu-commands-qualcomm_command-QualcommCommand-get_priority"></a>
#### 🅵 gpu\.commands\.qualcomm\_command\.QualcommCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="gpu-commands-qualcomm_command-QualcommCommand-execute"></a>
#### 🅵 gpu\.commands\.qualcomm\_command\.QualcommCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行高通Adreno GPU检测
<a name="gpu-core"></a>
## 🅼 gpu\.core
<a name="gpu-core-base"></a>
## 🅼 gpu\.core\.base

- **Classes:**
  - 🅲 [SystemType](#gpu-core-base-SystemType)
  - 🅲 [GPUVendor](#gpu-core-base-GPUVendor)
  - 🅲 [GPUType](#gpu-core-base-GPUType)
  - 🅲 [GPUInfo](#gpu-core-base-GPUInfo)
  - 🅲 [DetectionResult](#gpu-core-base-DetectionResult)
  - 🅲 [GPUDetectionCommand](#gpu-core-base-GPUDetectionCommand)
  - 🅲 [PlatformAdapter](#gpu-core-base-PlatformAdapter)

### Classes

<a name="gpu-core-base-SystemType"></a>
### 🅲 gpu\.core\.base\.SystemType

```python
class SystemType(Enum):
```

系统类型 - 扩展少
<a name="gpu-core-base-GPUVendor"></a>
### 🅲 gpu\.core\.base\.GPUVendor

```python
class GPUVendor(Enum):
```

GPU厂商 - 扩展多
<a name="gpu-core-base-GPUType"></a>
### 🅲 gpu\.core\.base\.GPUType

```python
class GPUType(Enum):
```

GPU类型
<a name="gpu-core-base-GPUInfo"></a>
### 🅲 gpu\.core\.base\.GPUInfo

```python
class GPUInfo:
```

GPU信息数据类 - 兼容原有API

**Functions:**

<a name="gpu-core-base-GPUInfo-to_dict"></a>
#### 🅵 gpu\.core\.base\.GPUInfo\.to\_dict

```python
def to_dict(self) -> Dict[str, Any]:
```

转换为字典 - 兼容原有格式
<a name="gpu-core-base-DetectionResult"></a>
### 🅲 gpu\.core\.base\.DetectionResult

```python
class DetectionResult:
```

检测结果数据类 - 兼容原有API

**Functions:**

<a name="gpu-core-base-DetectionResult-main_gpu"></a>
#### 🅵 gpu\.core\.base\.DetectionResult\.main\_gpu

```python
def main_gpu(self) -> Optional[GPUInfo]:
```

获取主GPU（优先离散，其次集成）
<a name="gpu-core-base-DetectionResult-to_dict"></a>
#### 🅵 gpu\.core\.base\.DetectionResult\.to\_dict

```python
def to_dict(self) -> Dict[str, Any]:
```

转换为字典 - 兼容原有格式
<a name="gpu-core-base-GPUDetectionCommand"></a>
### 🅲 gpu\.core\.base\.GPUDetectionCommand

```python
class GPUDetectionCommand(ABC):
```

GPU检测命令接口

**Functions:**

<a name="gpu-core-base-GPUDetectionCommand-execute"></a>
#### 🅵 gpu\.core\.base\.GPUDetectionCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行检测命令
<a name="gpu-core-base-GPUDetectionCommand-get_vendor"></a>
#### 🅵 gpu\.core\.base\.GPUDetectionCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```

返回厂商类型
<a name="gpu-core-base-GPUDetectionCommand-get_priority"></a>
#### 🅵 gpu\.core\.base\.GPUDetectionCommand\.get\_priority

```python
def get_priority(self) -> int:
```

优先级（数值越小越先执行）
<a name="gpu-core-base-PlatformAdapter"></a>
### 🅲 gpu\.core\.base\.PlatformAdapter

```python
class PlatformAdapter(ABC):
```

平台适配器接口

**Functions:**

<a name="gpu-core-base-PlatformAdapter-get_system_type"></a>
#### 🅵 gpu\.core\.base\.PlatformAdapter\.get\_system\_type

```python
def get_system_type(self) -> SystemType:
```

获取系统类型
<a name="gpu-core-base-PlatformAdapter-run_command"></a>
#### 🅵 gpu\.core\.base\.PlatformAdapter\.run\_command

```python
def run_command(self, cmd: str) -> tuple:
```

执行命令
<a name="gpu-core-base-PlatformAdapter-get_gpu_list"></a>
#### 🅵 gpu\.core\.base\.PlatformAdapter\.get\_gpu\_list

```python
def get_gpu_list(self) -> List[Dict[str, Any]]:
```

获取GPU原始列表
<a name="gpu-core-command_executor"></a>
## 🅼 gpu\.core\.command\_executor

- **Classes:**
  - 🅲 [CommandRegistry](#gpu-core-command_executor-CommandRegistry)
  - 🅲 [GPUCommandExecutor](#gpu-core-command_executor-GPUCommandExecutor)

### Classes

<a name="gpu-core-command_executor-CommandRegistry"></a>
### 🅲 gpu\.core\.command\_executor\.CommandRegistry

```python
class CommandRegistry:
```

命令注册器

**Functions:**

<a name="gpu-core-command_executor-CommandRegistry-register"></a>
#### 🅵 gpu\.core\.command\_executor\.CommandRegistry\.register

```python
def register(cls, command: GPUDetectionCommand):
```

注册命令
<a name="gpu-core-command_executor-CommandRegistry-get"></a>
#### 🅵 gpu\.core\.command\_executor\.CommandRegistry\.get

```python
def get(cls, vendor: GPUVendor) -> Optional[GPUDetectionCommand]:
```

获取命令
<a name="gpu-core-command_executor-CommandRegistry-get_all"></a>
#### 🅵 gpu\.core\.command\_executor\.CommandRegistry\.get\_all

```python
def get_all(cls) -> List[GPUDetectionCommand]:
```

获取所有命令（按优先级排序）
<a name="gpu-core-command_executor-CommandRegistry-clear"></a>
#### 🅵 gpu\.core\.command\_executor\.CommandRegistry\.clear

```python
def clear(cls):
```

清空所有命令
<a name="gpu-core-command_executor-GPUCommandExecutor"></a>
### 🅲 gpu\.core\.command\_executor\.GPUCommandExecutor

```python
class GPUCommandExecutor:
```

GPU命令执行器 - 核心业务逻辑

**Functions:**

<a name="gpu-core-command_executor-GPUCommandExecutor-__init__"></a>
#### 🅵 gpu\.core\.command\_executor\.GPUCommandExecutor\.\_\_init\_\_

```python
def __init__(self, system: str = None):
```

初始化执行器

**Parameters:**

- **system**: 系统类型 \(linux/windows/macos\)，None表示自动检测
<a name="gpu-core-command_executor-GPUCommandExecutor-detect_all"></a>
#### 🅵 gpu\.core\.command\_executor\.GPUCommandExecutor\.detect\_all

```python
def detect_all(self) -> DetectionResult:
```

检测所有GPU - 返回DetectionResult
<a name="gpu-core-command_executor-GPUCommandExecutor-detect_by_vendor"></a>
#### 🅵 gpu\.core\.command\_executor\.GPUCommandExecutor\.detect\_by\_vendor

```python
def detect_by_vendor(self, vendor: GPUVendor) -> List[GPUInfo]:
```

检测特定厂商的GPU
<a name="gpu-core-command_executor-GPUCommandExecutor-add_command"></a>
#### 🅵 gpu\.core\.command\_executor\.GPUCommandExecutor\.add\_command

```python
def add_command(self, command: GPUDetectionCommand):
```

动态添加命令（用于扩展）
<a name="gpu-core-command_executor-GPUCommandExecutor-remove_command"></a>
#### 🅵 gpu\.core\.command\_executor\.GPUCommandExecutor\.remove\_command

```python
def remove_command(self, vendor: GPUVendor):
```

移除命令
<a name="gpu-core-command_executor-GPUCommandExecutor-get_registered_vendors"></a>
#### 🅵 gpu\.core\.command\_executor\.GPUCommandExecutor\.get\_registered\_vendors

```python
def get_registered_vendors(self) -> List[GPUVendor]:
```

获取已注册的厂商列表
<a name="gpu-core-factory"></a>
## 🅼 gpu\.core\.factory

- **Classes:**
  - 🅲 [GPUDetectorFactory](#gpu-core-factory-GPUDetectorFactory)

### Classes

<a name="gpu-core-factory-GPUDetectorFactory"></a>
### 🅲 gpu\.core\.factory\.GPUDetectorFactory

```python
class GPUDetectorFactory:
```

GPU检测器工厂

**Functions:**

<a name="gpu-core-factory-GPUDetectorFactory-__init__"></a>
#### 🅵 gpu\.core\.factory\.GPUDetectorFactory\.\_\_init\_\_

```python
def __init__(self):
```
<a name="gpu-core-factory-GPUDetectorFactory-get_detector"></a>
#### 🅵 gpu\.core\.factory\.GPUDetectorFactory\.get\_detector

```python
def get_detector(self, lspci_line: str, gpu_name: str) -> Optional[BaseGPUDetector]:
```

根据lspci行获取合适的检测器
<a name="gpu-core-factory-GPUDetectorFactory-detect_all"></a>
#### 🅵 gpu\.core\.factory\.GPUDetectorFactory\.detect\_all

```python
def detect_all(self) -> DetectionResult:
```

检测所有GPU
<a name="gpu-gpu_detector"></a>
## 🅼 gpu\.gpu\_detector

- **Classes:**
  - 🅲 [GPUDetector](#gpu-gpu_detector-GPUDetector)

### Classes

<a name="gpu-gpu_detector-GPUDetector"></a>
### 🅲 gpu\.gpu\_detector\.GPUDetector

```python
class GPUDetector:
```

**Functions:**

<a name="gpu-gpu_detector-GPUDetector-__init__"></a>
#### 🅵 gpu\.gpu\_detector\.GPUDetector\.\_\_init\_\_

```python
def __init__(self):
```
<a name="gpu-gpu_detector-GPUDetector-gpu_detected"></a>
#### 🅵 gpu\.gpu\_detector\.GPUDetector\.gpu\_detected

```python
def gpu_detected(self) -> Dict[str, Any]:
```

检测GPU信息（独立显卡和集成显卡）

这是API文档中定义的接口，保持向后兼容

**Returns:**

- `Dict`: GPU检测结果字典
<a name="gpu-gpu_detector-GPUDetector-get_gpu_summary"></a>
#### 🅵 gpu\.gpu\_detector\.GPUDetector\.get\_gpu\_summary

```python
def get_gpu_summary(self) -> Dict[str, Any]:
```

获取GPU摘要信息

这是API文档中定义的接口

**Returns:**

- `Dict`: GPU摘要信息
<a name="gpu-vendor"></a>
## 🅼 gpu\.vendor
<a name="gpu-vendor-amd"></a>
## 🅼 gpu\.vendor\.amd

- **Classes:**
  - 🅲 [AMDDetector](#gpu-vendor-amd-AMDDetector)

### Classes

<a name="gpu-vendor-amd-AMDDetector"></a>
### 🅲 gpu\.vendor\.amd\.AMDDetector

```python
class AMDDetector(BaseGPUDetector):
```

AMD GPU检测器

**Functions:**

<a name="gpu-vendor-amd-AMDDetector-vendor"></a>
#### 🅵 gpu\.vendor\.amd\.AMDDetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="gpu-vendor-amd-AMDDetector-detect_from_lspci"></a>
#### 🅵 gpu\.vendor\.amd\.AMDDetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测AMD GPU
<a name="gpu-vendor-amd-AMDDetector-detect_driver_version"></a>
#### 🅵 gpu\.vendor\.amd\.AMDDetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测AMD驱动版本
<a name="gpu-vendor-amd-AMDDetector-detect_rocm_version"></a>
#### 🅵 gpu\.vendor\.amd\.AMDDetector\.detect\_rocm\_version

```python
def detect_rocm_version(self) -> Optional[str]:
```

检测ROCm版本
<a name="gpu-vendor-amd-AMDDetector-enhance_gpu_info"></a>
#### 🅵 gpu\.vendor\.amd\.AMDDetector\.enhance\_gpu\_info

```python
def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
```

增强AMD GPU信息
<a name="gpu-vendor-huawei"></a>
## 🅼 gpu\.vendor\.huawei

- **Classes:**
  - 🅲 [HuaweiDetector](#gpu-vendor-huawei-HuaweiDetector)

### Classes

<a name="gpu-vendor-huawei-HuaweiDetector"></a>
### 🅲 gpu\.vendor\.huawei\.HuaweiDetector

```python
class HuaweiDetector(BaseGPUDetector):
```

华为昇腾GPU检测器

**Functions:**

<a name="gpu-vendor-huawei-HuaweiDetector-vendor"></a>
#### 🅵 gpu\.vendor\.huawei\.HuaweiDetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="gpu-vendor-huawei-HuaweiDetector-detect_from_lspci"></a>
#### 🅵 gpu\.vendor\.huawei\.HuaweiDetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测华为昇腾GPU
<a name="gpu-vendor-huawei-HuaweiDetector-detect_driver_version"></a>
#### 🅵 gpu\.vendor\.huawei\.HuaweiDetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测昇腾驱动版本
<a name="gpu-vendor-huawei-HuaweiDetector-detect_ascend_version"></a>
#### 🅵 gpu\.vendor\.huawei\.HuaweiDetector\.detect\_ascend\_version

```python
def detect_ascend_version(self) -> Optional[str]:
```

检测CANN版本
<a name="gpu-vendor-huawei-HuaweiDetector-enhance_gpu_info"></a>
#### 🅵 gpu\.vendor\.huawei\.HuaweiDetector\.enhance\_gpu\_info

```python
def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
```

增强昇腾GPU信息
<a name="gpu-vendor-intel"></a>
## 🅼 gpu\.vendor\.intel

- **Classes:**
  - 🅲 [IntelDetector](#gpu-vendor-intel-IntelDetector)

### Classes

<a name="gpu-vendor-intel-IntelDetector"></a>
### 🅲 gpu\.vendor\.intel\.IntelDetector

```python
class IntelDetector(BaseGPUDetector):
```

Intel GPU检测器

**Functions:**

<a name="gpu-vendor-intel-IntelDetector-vendor"></a>
#### 🅵 gpu\.vendor\.intel\.IntelDetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="gpu-vendor-intel-IntelDetector-detect_from_lspci"></a>
#### 🅵 gpu\.vendor\.intel\.IntelDetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测Intel GPU
<a name="gpu-vendor-intel-IntelDetector-detect_driver_version"></a>
#### 🅵 gpu\.vendor\.intel\.IntelDetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测Intel驱动版本
<a name="gpu-vendor-nvidia"></a>
## 🅼 gpu\.vendor\.nvidia

- **Classes:**
  - 🅲 [NVIDIADetector](#gpu-vendor-nvidia-NVIDIADetector)

### Classes

<a name="gpu-vendor-nvidia-NVIDIADetector"></a>
### 🅲 gpu\.vendor\.nvidia\.NVIDIADetector

```python
class NVIDIADetector(BaseGPUDetector):
```

NVIDIA GPU检测器

**Functions:**

<a name="gpu-vendor-nvidia-NVIDIADetector-vendor"></a>
#### 🅵 gpu\.vendor\.nvidia\.NVIDIADetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="gpu-vendor-nvidia-NVIDIADetector-detect_from_lspci"></a>
#### 🅵 gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测NVIDIA GPU
<a name="gpu-vendor-nvidia-NVIDIADetector-detect_driver_version"></a>
#### 🅵 gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测NVIDIA驱动版本
<a name="gpu-vendor-nvidia-NVIDIADetector-detect_cuda_version"></a>
#### 🅵 gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_cuda\_version

```python
def detect_cuda_version(self) -> Optional[str]:
```

检测CUDA版本
<a name="gpu-vendor-nvidia-NVIDIADetector-detect_nvlink"></a>
#### 🅵 gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_nvlink

```python
def detect_nvlink(self) -> Dict[str, Any]:
```

检测NVLink状态
<a name="gpu-vendor-nvidia-NVIDIADetector-enhance_gpu_info"></a>
#### 🅵 gpu\.vendor\.nvidia\.NVIDIADetector\.enhance\_gpu\_info

```python
def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
```

增强NVIDIA GPU信息
<a name="gpu-vendor-utils"></a>
## 🅼 gpu\.vendor\.utils

- **Functions:**
  - 🅵 [run\_cmd\_safe](#gpu-vendor-utils-run_cmd_safe)
  - 🅵 [extract\_gpu\_name](#gpu-vendor-utils-extract_gpu_name)
  - 🅵 [get\_gpu\_memory](#gpu-vendor-utils-get_gpu_memory)
  - 🅵 [get\_gpu\_specs](#gpu-vendor-utils-get_gpu_specs)

### Functions

<a name="gpu-vendor-utils-run_cmd_safe"></a>
### 🅵 gpu\.vendor\.utils\.run\_cmd\_safe

```python
def run_cmd_safe(cmd: str, timeout: int = 5):
```

安全执行命令
<a name="gpu-vendor-utils-extract_gpu_name"></a>
### 🅵 gpu\.vendor\.utils\.extract\_gpu\_name

```python
def extract_gpu_name(line: str) -> str:
```

从 lspci 输出中提取干净的 GPU 名称
<a name="gpu-vendor-utils-get_gpu_memory"></a>
### 🅵 gpu\.vendor\.utils\.get\_gpu\_memory

```python
def get_gpu_memory(gpu_name: str, gpu_raw_line: Optional[str] = None) -> Optional[int]:
```

获取 GPU 显存大小（GB）
<a name="gpu-vendor-utils-get_gpu_specs"></a>
### 🅵 gpu\.vendor\.utils\.get\_gpu\_specs

```python
def get_gpu_specs(gpu_name: str) -> Optional[Dict[str, Any]]:
```

根据GPU名称获取完整规格
