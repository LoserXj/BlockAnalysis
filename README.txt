1.English Version
2.中文版

============================================
Second-order transaction network of phishing nodes
============================================
By InPlusLab, Sun Yat-sen University


================== References ==================

• Website
	http://xblock.pro/ethereum/

• Cite
	@misc{xblockEthereum,
		author = {Yuan, Zihao and Wu, Jiajing and Zheng, Zibin},
		title = {{XBLOCK Blockchain Datasets}: {InPlusLab} Ethereum Second-order Phishing Datasets},
		howpublished = {\url{http://xblock.pro/ethereum/}},
		month = Mar,
		year = 2020
	}


================== Change Log =================

• Version 1.0, released on 03/10/2020


=================== Source ====================

From https://etherscan.io crawled the transaction data of the target node from the deadline to 2019/12/31.


================ File Information =================


• Description
	The second-order transaction network dataset contains 1660 target phishing nodes and 1700 non-phishing nodes crawled from Etherscan.
	The second-order transaction network is divided into two parts. On the one hand, the csv files record the transaction information between the target node and its first-order transaction node. On the other hand, the csv files also record the transactions between each first-order transaction node and its corresponding second-order transaction node. information.


• Contents
	- Phishing first-order nodes
		Transaction information between a phishing node and its first-order transaction node.
		Size: 14.7MB
	- Phishing second-order nodes
		The transaction information between the first-order transaction node of the phishing node and its second-order transaction node.
		Size: 408MB
	- Normal first-order nodes
		Transaction information between a normal node and its first-order transaction node.
	 	Size: 38.6MB
	- Normal second-order nodes
		The transaction information between the first-order transaction node of the normal node and its second-order transaction node.
		Size: 1.24GB

* Notes * 
The first-order node folder directly stores the csv files that records the corresponding first-order transaction information of the node.
The second-order node folder contains a one-to-one correspondence with the target node, and each folder holds the corresponding second-order transaction information csv files. 



———————————— Phishing/Normal first-order nodes ———————————— 

• address.csv

	
	- Row:
		Each row represents the transaction information of the target node.
  
	- Column:
		1.TxHash : Transaction hash				
		2.BlockHeight : Height of block				
		3.TimeStamp : Transaction timestamp				
		4.From : Address of transaction initiating node				
		5.To : Address of transaction receiving node				
		6.Value : Transaction amount				


* Notes * 



===================Contact====================

Please contact Yuan Zihao (yuanzh7@mail2.sysu.edu.cn) for any questions about the dataset.



============================================
以太坊钓鱼节点二阶交易网络数据集
============================================
By InPlusLab, 中山大学


==================== 参考 =====================

• 相关网站
	http://xblock.pro/ethereum/

• 引用
    @misc{xblockEthereum,
		author = {Yuan, Zihao and Wu, Jiajing and Zheng, Zibin},
		title = {{XBLOCK Blockchain Datasets}: {InPlusLab} Ethereum Second-order Phishing Datasets},
		howpublished = {\url{http://xblock.pro/ethereum/}},
		month = Mar,
		year = 2020
	}


=================== 变更日志 ====================

• 版本 1.0, 发布于 03/10/2020


=================== 数据来源 ====================

从 https://etherscan.io 爬取了到2019/12/31的目标节点相关交易数据. 


=================== 文件信息 ====================


• 描述
	该二阶交易网络数据集为从Etherscan上爬取的1660个目标钓鱼节点以及1700个非钓鱼节点的二阶交易网络信息。
	该二阶交易网络分为两部分，以csv形式记录了钓鱼节点与其一阶交易节点的之间交易信息，以及各个一阶交易节点与其对应的二阶交易节点之间的交易信息。


• 内容
	- 钓鱼一阶节点
		钓鱼节点与其一阶交易节点之间的交易信息。
		大小: 14.7MB
	- 钓鱼二阶节点
		钓鱼节点一阶交易节点与其二阶交易节点之间的交易信息。
		大小: 408MB
	- 非钓鱼一阶节点
		非钓鱼节点与其一阶交易节点之间的交易信息。
	 	大小: 38.6MB
	- 非钓鱼二阶节点
		非钓鱼节点一阶交易节点与其二阶交易节点之间的交易信息。
		大小: 1.24GB

* 注释 * 
一阶节点文件夹中，直接保存着记录节点相应一阶交易信息的csv文件
二阶节点文件夹中，包含了与目标节点一一对应的文件夹，每个文件夹中保存着相应二阶交易信息的csv文件



———————————— 钓鱼/非钓鱼一阶节点 ———————————— 

• address.csv


	- 行:
		每一行代表了目标节点参与的一次交易信息。
  
	- 列:
		1.TxHash :  交易哈希值
		2.BlockHeight :  交易所在区块高度
		3.TimeStamp :  交易时间戳	
		4.From :  交易发起节点地址
		5.To : 	交易接收节点地址
		6.Value : 交易金额		
		总和: 6 列


* 注释 * 




==================== 联系 =====================

若对数据集有任何问题请联系 袁子豪 (yuanzh7@mail2.sysu.edu.cn)。