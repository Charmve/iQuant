#!/bin/bash

# 判断当前目录是否存在BUILD文件
if [ ! -f "./BUILD" ]; then
    # 如果不存在，则创建BUILD文件
    touch ./BUILD
fi

# 遍历子目录，查找是否存在BUILD文件
for dir in $(find . -type d); do
    if [ "${dir}" != "." ]; then
        if [ ! -f "${dir}/BUILD" ]; then
            # 如果不存在，则创建BUILD文件
            touch "${dir}/BUILD"
        fi
    fi
done
