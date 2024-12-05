import gdown

# Google Drive 文件的共享链接
drive_link = "https://drive.google.com/file/d/1fjZZboWTeADwr1QBqGp1SVEZ54it2bHR/view?usp=drive_link"

# 提取文件ID
file_id = drive_link.split('/d/')[1].split('/')[0]

# 生成可直接下载的链接
download_url = f"https://drive.google.com/uc?id={file_id}"

# 保存的文件名
output_filename = "sbcdata.csv"

# 下载文件
gdown.download(download_url, output_filename, quiet=False)

print(f"文件已下载到当前目录，文件名为: {output_filename}")
