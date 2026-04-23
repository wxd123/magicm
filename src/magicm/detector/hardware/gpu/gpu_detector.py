# detector/hardware/gpu/gpu_detecter.py
from typing import Dict, Any
from .core.command_executor import GPUCommandExecutor




class GPUDetector: 

    def __init__(self):
        # 全局执行器实例
        self._executor = None

    def _get_executor(self):
        """获取全局执行器"""
        
        if self._executor is None:
            self._executor = GPUCommandExecutor()
        return self._executor


    def gpu_detected(self) -> Dict[str, Any]:
        """
        检测GPU信息（独立显卡和集成显卡）
        
        这是API文档中定义的接口，保持向后兼容
        
        Returns:
            Dict: GPU检测结果字典
        """
        executor = self._get_executor()
        result = executor.detect_all()
        return result.to_dict()


    def get_gpu_summary(self) -> Dict[str, Any]:
        """
        获取GPU摘要信息
        
        这是API文档中定义的接口
        
        Returns:
            Dict: GPU摘要信息
        """
        executor = self._get_executor()
        result = executor.detect_all()
        
        return {
            'total_count': len(result.all_gpus),
            'discrete_count': 1 if result.discrete_gpu else 0,
            'integrated_count': 1 if result.integrated_gpu else 0,
            'main_gpu': result.gpu_name,
            'gpu_list': [gpu.to_dict() for gpu in result.all_gpus],
            'vendors': list(set(gpu.vendor.value for gpu in result.all_gpus if gpu.vendor))
        }


# 全局单例实例定义
gpu_detector: GPUDetector = GPUDetector
