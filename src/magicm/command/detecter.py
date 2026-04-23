#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/command/detecter.py
"""
magicm CLI 硬件检测工具
"""

import sys
import os

from magicm.detector.software.system.sys_detecter import detect as sys_detecter
from magicm.detector.software.environment.env_detecter import detect as env_detecter
from magicm.detector.hardware.cpu import cpu_detecter
from magicm.detector.hardware.gpu import gpu_detector
from magicm.detector.hardware.mem import mem_detecter


class DetectCommand:
    """硬件检测命令类"""
    
    def __init__(self):
        """初始化检测命令"""
        self.system_info = {}
        self.cpu_info = {}
        self.gpu_info = {}
        self.memory_info = {}
        self.env_info = {}
    
    def get_env_info(self):
        """获取虚拟环境信息"""
        try:
            env_info = env_detecter()
        except Exception as e:
            env_info = {'env_type': 'unknown'}
        self.env_info = env_info
        return env_info
    
    def get_system_info(self):
        """获取系统信息"""
        try:
            system_info = sys_detecter()
            if not system_info or not isinstance(system_info, dict):
                system_info = {"name": "未知", "pretty_name": "未知系统"}
        except Exception as e:
            system_info = {"name": "未知", "pretty_name": "未知系统"}
        
        self.system_info = system_info
        return system_info
    
    def get_cpu_info(self):
        """获取CPU信息"""
        try:
            cpu_info = cpu_detecter.cpu_detected()
            if not cpu_info or not isinstance(cpu_info, dict):
                cpu_info = {"model": "未知", "simple_model": "未知CPU", "cores": "未知"}
        except Exception as e:
            cpu_info = {"model": "未知", "simple_model": "未知CPU", "cores": "未知"}
        
        self.cpu_info = cpu_info
        return cpu_info
    
    def get_gpu_info(self):
        """获取GPU信息"""
        try:
            gpu_result = gpu_detector.gpu_detected()
            
            gpu_info = {
                "name": "未知", 
                "memory_gb": 0, 
                "driver_version": "未知",
                "type": "unknown"
            }
            
            if gpu_result and isinstance(gpu_result, dict):
                if gpu_result.get("discrete_gpu"):
                    gpu_info["name"] = gpu_result["discrete_gpu"]
                elif gpu_result.get("integrated_gpu"):
                    gpu_info["name"] = gpu_result["integrated_gpu"]
                elif gpu_result.get("gpu_name"):
                    gpu_info["name"] = gpu_result["gpu_name"]
                
                if gpu_result.get("driver_version"):
                    gpu_info["driver_version"] = gpu_result["driver_version"]
                
                all_gpus = gpu_result.get("all_gpus", [])
                if all_gpus and len(all_gpus) > 0:
                    first_gpu = all_gpus[0]
                    if first_gpu.get("memory_gb"):
                        gpu_info["memory_gb"] = first_gpu["memory_gb"]
        except Exception as e:
            pass
        
        self.gpu_info = gpu_info
        return gpu_info
    
    def get_memory_info(self):
        """获取内存信息"""
        try:
            memory_info = mem_detecter.mem_detected()
            if not memory_info or not isinstance(memory_info, dict):
                memory_info = {"total_gb": 0, "total_mb": 0, "total_str": "未知"}
        except Exception as e:
            memory_info = {"total_gb": 0, "total_mb": 0, "total_str": "未知"}
        
        self.memory_info = memory_info
        return memory_info
    
    def detect(self):
        """主函数：顺序调用各检测模块，然后交给 display 显示"""
        print("\n🔍 正在检测硬件信息...\n")
        
        # 1. 操作系统检测
        self.get_system_info()
        
        # 2. CPU 检测
        self.get_cpu_info()
        
        # 3. GPU 检测
        self.get_gpu_info()
        
        # 4. 内存检测
        self.get_memory_info()
        
        # 5. 虚拟环境检测
        self.get_env_info()
        
        return {
            'system': self.system_info,
            'cpu': self.cpu_info,
            'gpu': self.gpu_info,
            'mem': self.memory_info,
            'env': self.env_info
        }
    
    def display(self):
        """显示检测结果"""
        result = self.detect()
        
        print("\n" + "="*50)
        print("📊 硬件检测结果")
        print("="*50)
        
        # 显示系统信息
        print(f"\n💻 操作系统: {result['system'].get('pretty_name', result['system'].get('name', '未知'))}")
        
        # 显示CPU信息
        cpu_name = result['cpu'].get('simple_model', result['cpu'].get('model', '未知'))
        cpu_cores = result['cpu'].get('cores', '未知')
        print(f"🖥️  CPU: {cpu_name} (核心数: {cpu_cores})")
        
        # 显示GPU信息
        gpu_name = result['gpu'].get('name', '未知')
        vram = result['gpu'].get('memory_gb', 0)
        driver = result['gpu'].get('driver_version', '未知')
        print(f"🎮 GPU: {gpu_name} (显存: {vram}GB, 驱动: {driver})")
        
        # 显示内存信息
        mem_gb = result['mem'].get('total_gb', 0)
        print(f"💾 内存: {mem_gb}GB")
        
        # 显示虚拟环境信息
        env_type = result.get('env', {}).get('env_type', '未知')
        print(f"🐍 虚拟环境: {env_type}")
        
        print("\n" + "="*50)


# 保持向后兼容的函数接口
def detect():
    """向后兼容的函数接口"""
    cmd = DetectCommand()
    return cmd.detect()

# 全局单例实例
detect_command: DetectCommand = DetectCommand()