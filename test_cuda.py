import paddle
import os

print(f"Paddle version: {paddle.__version__}")
print(f"Is GPU available: {paddle.is_compiled_with_cuda()}")

# ตรวจสอบ CUDA
try:
    print(f"CUDA version: {paddle.version.cuda()}")
    print(f"Device count: {paddle.device.cuda.device_count()}")
    if paddle.device.cuda.device_count() > 0:
        print(f"Current device: {paddle.device.get_device()}")
        print(f"Device name: {paddle.device.cuda.get_device_name()}")
except:
    print("CUDA not properly configured")

# ตรวจสอบ environment variables
print(f"CUDA_VISIBLE_DEVICES: {os.environ.get('CUDA_VISIBLE_DEVICES', 'Not set')}")