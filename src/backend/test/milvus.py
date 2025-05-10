from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
import numpy as np


# 连接Milvus
def connect_milvus(host='104.171.203.178', port='19530'):
    try:
        connections.connect(alias="default", host=host, port=port)
        print(f"成功连接到Milvus服务器: {host}:{port}")
        return True
    except Exception as e:
        print(f"连接失败: {e}")
        return False


# 创建集合
def create_collection(collection_name, dim=128):
    if utility.has_collection(collection_name):
        print(f"集合 {collection_name} 已存在")
        return False

    # 定义字段
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=dim),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=512)
    ]

    # 创建集合
    schema = CollectionSchema(fields=fields, description="示例向量集合")
    collection = Collection(name=collection_name, schema=schema)
    print(f"成功创建集合: {collection_name}")
    return collection


# 插入向量数据
def insert_vectors(collection, texts, vectors):
    data = [
        vectors,  # 向量数据
        texts  # 对应的文本描述
    ]

    insert_result = collection.insert(data)
    collection.flush()  # 刷新内存，确保数据写入
    print(f"成功插入 {len(texts)} 条数据")
    return insert_result


# 创建向量索引
def create_index(collection, index_params=None):
    if index_params is None:
        # 默认使用IVF_FLAT索引
        index_params = {
            "metric_type": "L2",
            "index_type": "IVF_FLAT",
            "params": {"nlist": 128}
        }

    collection.create_index(field_name="embedding", index_params=index_params)
    print("索引创建成功")


# 搜索相似向量
def search_vectors(collection, query_vector, top_k=10):
    # 加载集合到内存
    collection.load()

    # 搜索参数
    search_params = {
        "metric_type": "L2",
        "params": {"nprobe": 10}
    }

    # 执行搜索
    results = collection.search(
        data=[query_vector],
        anns_field="embedding",
        param=search_params,
        limit=top_k,
        output_fields=["text"]
    )

    return results


# 删除集合
def drop_collection(collection_name):
    if utility.has_collection(collection_name):
        utility.drop_collection(collection_name)
        print(f"集合 {collection_name} 已删除")
    else:
        print(f"集合 {collection_name} 不存在")


# 主函数示例
def main():
    COLLECTION_NAME = "example_collection"
    DIMENSION = 128  # 向量维度

    # 连接Milvus
    if not connect_milvus():
        return



    # 创建集合
    collection = create_collection(COLLECTION_NAME, DIMENSION)
    if not collection:
        collection = Collection(COLLECTION_NAME)
    print("连接成功...")

    try:
        # 生成示例数据
        texts = ["苹果", "香蕉", "橙子", "西瓜", "草莓"]
        vectors = [np.random.random(DIMENSION).tolist() for _ in range(len(texts))]

        # 插入数据
        insert_vectors(collection, texts, vectors)

        # 创建索引
        create_index(collection)

        # 搜索示例
        query_vector = np.random.random(DIMENSION).tolist()
        results = search_vectors(collection, query_vector)

        # 输出搜索结果
        print("\n搜索结果:")
        for hit in results[0]:
            print(f"ID: {hit.id}, 距离: {hit.distance}, 文本: {hit.entity.get('text')}")

    finally:
        # 清理资源（可选）
        collections = utility.list_collections()
        print("所有集合名称：", collections)
        drop_collection(COLLECTION_NAME)
        collections = utility.list_collections()
        print("所有集合名称：", collections)


if __name__ == "__main__":
    main()
