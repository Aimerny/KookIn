# KookIn

使用[KookAPI](https://github.com/Aimerny/KookAPI)实现的MCDR服务器管理插件

> 该插件的功能移植自[QQ Chat](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/qq_chat)插件

## 功能介绍

### MCDR端

1. 发送消息到指定Kook频道组
2. 将所有MC的聊天消息同步到指定Kook频道组中

### Kook端

1. 查看MC服务器中在线玩家列表
2. 离线时向服务器中发送消息
3. (TODO)管理服务器白名单 **(添加/移除/关闭/开启)**
4. (TODO)远程执行服务端指令
5. (TODO)远程执行MCDR指令

## 开始
由于Kook没有对频道的唯一ID显式提供, 我们需要经过一些准备工作才能拿到对应的频道ID
1. 启动MCDR服务器并加载插件
2. 调用`!!kkchans <关键字>`指令获取机器人加入的所有频道名称与频道ID
3. 根据频道ID配置插件频道信息,重新加载配置


## 配置项

`$MCDR/config/kookin/conf.json`

| 配置项               | 配置说明       | 类型                 | 示例               | 
|-------------------|------------|--------------------|------------------|
| admin_channel     | 服务器管理频道    | Array[channelInfo] | -                |
| public_channel    | 服务器公共频道    | Array[channelInfo] | -                |
| sync_chat_channel | 服务器消息同步频道  | Array[channelInfo] | -                |
| channel_name      | 频道名称备注     | string             | 频道A              |
| channel_id        | 频道ID       | string             | 获取方式见上           |
| admins            | 管理员        | Array[string]      | ["Aimerny#0476"] |
| server_name       | Kook展示服务器名 | string             | Survival         |
> 1. 服务器管理频道中的成员默认都视为管理员,可不加入admins列表中
> 2. 只有使用`!!kk` 指令的消息才会被发送到服务器公共频道中
> 3. 在服务器公共频道中的消息只有使用/mc指令的消息才会发送到服务器中
> 4. 所有游戏内消息都会被发送至消息同步频道中,在消息同步频道中发送任何消息也会同步到游戏中

## 指令预览

### MCDR端指令

```
!!kk <msg> #发送消息到指定Kook服务器
!!kkchans <search_key> #搜索当前机器人加入的频道Id,search_key为名称过滤
``` 

```
# kkchans 返回格式说明
[${服务器名称}]=>[${频道名称}]=>[${频道id}]
```

### Kook端指令

```
/help      =>   查询指令
/bind      =>   成员绑定
/whitelist =>   白名单管理
/list      =>   在线玩家列表
```

#### 绑定相关

```
/bind <mc_id>         => 绑定MC
/bind clear @Kook成员 => 清除指定用户绑定信息(管理员可用)
/bind list            => 查看已绑定列表(管理员可用)
```