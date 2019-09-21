# Node

## 描述

所有要绘制在界面上的对象继承于此

## 目的

## 定义详情

### 属性
 
- 公有

- 私有
  - Node parent
  - List(Node) childrenList
  - Vector2 positon
  - int order
  - Vector2 rotation
  - Vector2 scale
  - bool enabled
  - int opacity

### 方法

- 公有
  - T Create()
  - AddChild(Node)
  - void Draw()
  - Vector2 GetPosition()
  - Vector2 GetWorldPosition()
  - int GetOrder()
  - Vector2 GetScale
  - Vector2 GetRotation()
  - bool Enabled()
  - void removeFromParent()
  - int GetOpacity()
- 私有
  - Node GetParent()
  - void init()
  - void SortChildrenByOrder()

  
