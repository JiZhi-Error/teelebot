# Function (teelebot version >= v2.5.3)

#### bot API methods

可用方法名及参数同Telegram官方文档保持一致：[**Telegram Bot API**](https://core.telegram.org/bots/api)



***特殊情况：***

1.Media相关方法

* *bot.sendMediaGroup*()
* *bot.editMessageMedia*()

*使用以上两个方法上传本地文件时，请使用参数 `files` ，格式请参考 [inputmedia](https://core.telegram.org/bots/api#inputmedia)*

2.消息发送类型方法

当使用消息发送类型方法发送消息后，若需要定时删除消息，可使用参数 `del_msg_after` ，范围为0~900。比如，当 `del_msg_after=3` 时，消息将在3秒后被删除。

3.以多线程方式执行方法

若需要不阻塞地调用方法，请使用参数 `run_in_thread` ，该参数默认值为`False` 。比如，当 `run_in_thread=True` 时，方法将在线程池中执行。

**注意**：若方法在线程池中执行，将不返回Telegram官方接口的响应数据。



#### teelebot methods

* bot.message_deletor(*time_gap*: int, *chat_id*: str, *message_id*: str) -> str
* bot.timer(*time_gap*: int, *func*: Callable[..., None], **args*: tuple) -> str
* bot.path_converter(*path*: str) -> str
* bot.join_plugin_path(*path*: str, *plugin_name*: str = None) -> str
* bot.getChatCreator(*chat_id*: str) -> Union[bool, dict]
* bot.getChatMemberStatus(*chat_id*: str, *user_id*: str) -> Union[bool, str]
* bot.getFileDownloadPath(*file_id*: str) -> Union[bool, str]
* bot.getChatAdminsUseridList(*chat_id*, *skip_bot*: bool = True, *privilege_users*: list = None) -> Union[bool, list]
* bot.schedule.add(*gap*: int, *func*: Callable[..., None], **args*: tuple) -> Tuple[bool, str]
* bot.schedule.status() -> Tuple[bool, dict]
* bot.schedule.find(*uid*: str) -> Tuple[bool, str]
* bot.schedule.delete(*uid*: str) -> Tuple[bool, str]
* bot.schedule.clear() -> Tuple[bool, str]
* bot.buffer.status() -> Tuple[bool, dict]
* bot.buffer.sizeof(*plugin_name*: str = None) -> Tuple[bool, Union[str, int]]
* bot.buffer.create(*self*, *plugin_name*: str = None, *buffer_name*: str = "default") -> Tuple[bool, Union[str, tuple, any]]
* bot.buffer.drop(*self*, *plugin_name*: str = None, *buffer_name*: str = None) -> Tuple[bool, Union[str, tuple, any]]
* bot.buffer.show(*self*, *plugin_name*: str = None) -> Tuple[bool, Union[str, tuple, dict]]
* bot.buffer.insert(*self*, *plugin_name*: str = None, *buffer_name*: str = "default", *data*: dict = {}) -> Tuple[bool, Union[str, tuple]]
* bot.buffer.delete(*self*, *plugin_name*: str = None, *buffer_name*: str = "default", *idx*: int = None, *conditions*: dict = {}) -> Tuple[bool, Union[str, tuple, any]]
* bot.buffer.update(*self*, *plugin_name*: str = None, *buffer_name*: str = "default", *idx*: int = None, *conditions*: dict = {}, *data*: dict = {}) -> Tuple[bool, Union[str, tuple, any]]
* bot.buffer.select(*self*, *plugin_name*: str = None, *buffer_name*: str = "default", *idx*: int = None, *conditions*: dict = {}) -> Tuple[bool, Union[str, tuple, dict, any]]
* bot.buffer.clear(*self*, *plugin_name*: str = None, *buffer_name*: str = None) -> Tuple[bool, Union[str, tuple, any]]
* bot.metadata.read(*plugin_name*: str = None, *plugin_dir*: str = None) -> Tuple[bool, Union[dict, str]]
* bot.metadata.write(*metadata*: dict, *plugin_name*: str = None, *plugin_dir*: str = None) -> Tuple[bool, Union[dict, str]]
* bot.metadata.template(*version*: str = None) -> Tuple[bool, Union[dict, str]]



#### teelebot properties

*  bot.root_id
*  bot.bot_id
*  bot.author
*  bot.version
*  bot.plugin_dir
*  bot.plugin_bridge
*  bot.uptime
*  bot.response_times
*  bot.response_chats
*  bot.response_users
*  bot.proxies



