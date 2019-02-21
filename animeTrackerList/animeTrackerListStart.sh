#!/bin/sh
# 调用帮助
# $ bash ./animeTrackerListStart.sh --help
# 在screen中打开服务器
# $ bash ./animeTrackerListStart.sh -r
# 结束现有开启的服务器
# $ bash ./animeTrackerListStart.sh -kf
# 查看服务器运行状态
# $ bash ./animeTrackerListStart.sh -s
# 将后台的screen调至前台
# $ bash ./animeTrackerListStart.sh -f


if [ "$1" == --help ];then
    printf " ==========================================\n"
    printf " -r\t如果存在animeTrackerListStart则重新启动\n"
    printf " -kf\t如果存在animeTrackerListStart则kill掉该进程\n"
    printf " -s\t查看animeTrackerListStart的状态\n"
    printf " -f\t将animeTrackerListStart调至前台\n"
    printf " --help\t帮助\n"
    printf " ------------------------------------------\n"
    exit 0
fi

declare -a pid_screen
declare pid
if [ "$1" == -f ];then
    pid_screen=$(screen -list | grep 'animeTrackerListStart'|cut -d . -f 1)
    printf ${pid_screen}
    if [ -n ${pid_screen} ];then

    if [ ${#pid_screen[*]} -eq 1 ];then
        screen  -r animeTrackerListStart
    else
        printf "\t有多个animeTrackerListStart\n"
        screen -list
    fi
    else
        printf "\t后台没有animeTrackerListStart\n"
    exit 0
    fi
    exit 0
fi

#查询是否已经开启animeTrackerListStart
pid=$(ps -ef | grep forge-1.10.2-12 | egrep -v 'grep|screen|tee|SCREEN' | awk '{ printf $2}')


if [ -n "$1" ]; then
    if [ "$1" == -r ];then
    if [ -n "$pid"  ];then
        kill $pid
    fi
    #       echo "kill"

    elif [ "$1" == -kf ];then
    if [ -n "$pid" ];then
        kill $pid
    fi

    pid_screen=$(screen -list | grep 'animeTrackerListStart'|cut -d . -f 1 )
    if [ ${#pid_screen[*]} -eq 1 ];then
        kill $pid_screen

        exit 0
    fi
    elif [ "$1" == -ka ];then
    if [ -n "$pid" ];then
        kill $pid
    fi
        pid_screen=$(screen -list | grep 'animeTrackerListStart'|cut -d . -f 1)
        kill $pid_screen

        exit 0
    elif [ "$1" ==  -s ]; then
    if [ -n "$pid" ]; then
        printf "\t animeTrackerListStart在运行\n"
        ps -ef | grep forge-1.10.2-12 | egrep -v 'grep|screen|tee|SCREEN'
    else
        printf "\t animeTrackerListStart没有运行\n"
    fi
    exit 0
    else
    printf "\t参数不正确\n使用--help可查看参数\n"

    exit 0
    fi
else
    printf "\t参数不正确\n使用--help可查看参数\n"

    exit 0
fi


unset pid
unset pid_screen
date >> ./animeTrackerListStart.log
screen  -R animeTrackerListStart python animeTrackerList.py nogui| tee -a ./animeTrackerListStart.log
