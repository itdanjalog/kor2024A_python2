'''

- 이진 트리
    - 데이터를 저장하는 비선형 자료구조( 앞/뒤 데이터가 1:N 관계 )
    - 각 노드가 최대 2개의 자식 노드를 가질수 있는 트리 구조
    - 왼쪽 자식노드의 데이터는 부모 노드보다 작다. 오른쪽 자식노드의 데이터는 부모 노드보다 크다.
    - 일상생활 : 데이터 검색 , 정렬 , 파일 시스템 등등

        - 용어
        1. 노드 : 데이터가 들어가는 공간
        2. 부모노드 : 특정 노드의 바로 위 노드
        3. 자식노드 : 특정 노드의 바로 아래에 있는 노드들, 이진트리에서는 최대 2개를 가질수 있다.
        4. 루트노드 : 트리의 맨위에 있는 노드로, 루트노드는 시작하는 경로를 통해 접근한다.
        5. 깊이 : 루트노드에서 특정 노드까지의 경로의 길이
        6. 높이 : 트리의 최대 깊이 , 가장 깊은 노드의 길이


이진트리(Binary Tree)는 각 노드가 최대 두 개의 자식 노드를 가질 수 있는 계층적인 데이터 구조입니다.
이진트리는 매우 중요하며 다양한 알고리즘과 데이터 구조에서 사용됩니다.
여기에서 이진트리에 대한 정의와 그 사용 이유에 대해 알아보겠습니다.

루트 노드(root node): 트리의 시작 노드로, 다른 모든 노드는 이 루트 노드에서부터 시작됩니다.
부모 노드(parent node): 다른 노드들의 상위에 있는 노드를 의미합니다.
자식 노드(child node): 부모 노드에 의해 생성된 하위 노드를 의미합니다. 이진트리에서 각 노드는 최대 두 개의 자식 노드를 가질 수 있습니다.


데이터 정렬 및 검색:
이진트리는 데이터를 효율적으로 정렬하고 검색할 수 있는 구조입니다.
이진 탐색 트리(Binary Search Tree, BST)는 모든 노드가 왼쪽 자식 노드보다 작고 오른쪽 자식 노드보다 큰 특성을 가지므로,
정렬된 상태를 유지하면서 검색 연산을 평균 O(log n)의 시간 복잡도로 수행할 수 있습니다.

자료 구조의 효율성: 데이터의 삽입, 삭제, 검색 연산을 효율적으로 수행할

계층적 데이터 표현:계층적인 데이터를 표현하는 데 이진트리가 자연스럽게 적합합니다.
예를 들어 파일 시스템이나 조직도와 같은 계층적 구조를 트리로 표현할 수 있습니다.

재귀적 구조:이진트리는 재귀적으로 정의되며, 재귀 알고리즘을 구현하는 데 유용합니다.
전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)와
같은 트리 순회 방식은 재귀적인 접근을 요구하며,
이진트리를 이해하고 구현하는 데 중요한 역할을 합니다.

효율적인 메모리 관리:
이진트리는 데이터의 추가 및 삭제 시에 메모리를 효율적으로 사용할 수 있습니다.
각 노드는 고정된 수의 자식 노드를 가지므로 메모리 할당과 해제가 비교적 단순하게 처리될 수 있습니다.

'''


# 자료구조 [ 데이터를 저장하는 방법 : 스택 , 큐 ]


# 이진트리 :  각각의 노드가 최대 두 개의 자식 노드를 가지는 트리 자료 구조로
# 1. 컴퓨터 폴더
# 2. 정렬과 검색
# 3. 하나의 노드의 왼쪽자식노드 와 오른쪽자식노드

# 파이썬에서 완전이진트리의 생성 예
class TreeNode() :
    def __init__(self):
        self.left = None    # 왼쪽노드의 위치
        self.data = None    # 현재노드의 값
        self.right = None   # 오른쪽노드의 위치

node1 = TreeNode() # 해당클래스의 객체 생성
node1.data = "유재석"

node2 = TreeNode() # 해당클래스의 객체 생성
node2.data = "강호동"
node1.left = node2

node3 = TreeNode()
node3.data = "신동엽"
node1.right = node3

node4 = TreeNode()
node4.data = "서장훈"
node2.left = node4

node5 = TreeNode()
node5.data ="김희철"
node2.right = node5

node6 = TreeNode
node6.data ="우원재"
node3.left = node6

print( node1.data , end=" ")
print( )
print( node1.left.data ,"   " + node1.right.data )
print()
print( node1.left.left.data, " " , node1.left.right.data , " ", node1.right.left.data)
