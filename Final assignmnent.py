import heapq


class ExamBookingSystem:
    """System to process and manage exam bookings using BST, Max-Heap, and Hash Table."""

    def __init__(self):
        self.location_bst = None  # Root of the Binary Search Tree (BST)
        self.max_heap = []  # Max-Heap for exam prioritization
        self.hash_table = {}  # Hash Table for fast lookup by course ID

    """ Requirement 1: Find exams within a given range of rooms, for example, rooms 40–65
        Data Structure Used: BST - Binary Search Tree
        Reason: BST will allow us to store locations sorted as keys. 
        Retrieving all the locations within a range like 40–65 will be highly efficient by doing 
        an in-order traversal which may filter the nodes in that range."""

    class BSTNode:
        """Node structure for the Binary Search Tree."""
        def __init__(self, location, exam_data):
            self.location = location  # Key: Exam location
            self.exam_data = exam_data  # Value: Exam details
            self.left = None  # Left child
            self.right = None  # Right child

    def insert_bst(self, location, exam_data):
        """Insert an exam into the BST based on location."""
        def _insert(node, location, exam_data):
            if not node:  # Base case: Insert new node
                return self.BSTNode(location, exam_data)
            if location < node.location:  # Go left if location is smaller
                node.left = _insert(node.left, location, exam_data)
            else:  # Go right if location is greater or equal
                node.right = _insert(node.right, location, exam_data)
            return node

        self.location_bst = _insert(self.location_bst, location, exam_data)

    def find_exams_in_range(self, low, high):
        result = []  # List to store exams in range

        def _in_order(node):
            """In-order traversal to filter exams in the range."""
            if not node:
                return
            if low <= node.location <= high:  # Check if location is in range
                result.append(node.exam_data)
            if node.location > low:  # Check left subtree
                _in_order(node.left)
            if node.location < high:  # Check right subtree
                _in_order(node.right)

        _in_order(self.location_bst)
        return result

    """Requirement 2: List exams in descending order of students that would appear in it.
                 Data Structure used: Max-Heap
                 Reason: In this context, a Max-Heap is best because getting the maximum value-in this case, 
                the exam with the most students-can be achieved quickly. In a heap, insertion and retrieval 
                operations are logarithmic in nature; thus, it fits well here."""


    def insert_heap(self, exam_data):
        """Insert an exam into the max-heap based on the number of students."""
        # Use negative count for max-heap behavior with Python's min-heap
        heapq.heappush(self.max_heap, (-exam_data["num_students"], exam_data))

    def get_highest_priority_exam(self):
        """Retrieve the exam with the highest number of students."""
        if not self.max_heap:
            return None  # Return None if heap is empty
        return heapq.heappop(self.max_heap)[1]  # Return exam data

    """ 
        Requirement 3: Quick storage and retrieval of exams using the unique course ID
        Data Structure Used: Hash Table
        Reason: Hash tables enable average constant time-the case complexity for storing values
        and retrieving them using unique keys; hence, it's ideal to deal with course id processing.
    """

    def store_exam_by_id(self, course_id, exam_data):
        """Store an exam in the hash table using its unique course ID."""
        self.hash_table[course_id] = exam_data

    def get_exam_by_id(self, course_id):
        """Retrieve an exam from the hash table using its course ID."""
        return self.hash_table.get(course_id, None)  # Return None if ID not found


# ===== Testing the System =====
if __name__ == "__main__":
    system = ExamBookingSystem()

    # Test exams
    exams = [
        {"course_id": "ABC-123-456", "location": 50, "date": "2024-12-10", "num_students": 100},
        {"course_id": "DEF-456-789", "location": 60, "date": "2024-12-11", "num_students": 120},
        {"course_id": "GHI-789-012", "location": 40, "date": "2024-12-12", "num_students": 80},
        {"course_id": "JKL-012-345", "location": 65, "date": "2024-12-13", "num_students": 150},
        {"course_id": "MNO-345-678", "location": 30, "date": "2024-12-14", "num_students": 70},
    ]

    # Insert exams into the system
    for exam in exams:
        system.insert_bst(exam["location"], exam)  # BST insertion
        system.insert_heap(exam)  # Max-Heap insertion
        system.store_exam_by_id(exam["course_id"], exam)  # Hash Table insertion

    # ===== Below are the Test Cases of exam booking system =====

    # Test Case 1: Finding exams in location range 30–65
    print("Test Case 1: Exams in location range 30–65:")
    print(system.find_exams_in_range(30, 65))

    # Test Case 2: Get exam with the highest priority (most students)
    print("Test Case 2: Exam with the highest number of students:")
    print(system.get_highest_priority_exam())

    # Test Case 3: Retrieving exam by course ID
    print("Test Case 3: Retrieve exam with ID 'DEF-456-789':")
    print(system.get_exam_by_id("DEF-456-789"))

    # Additional Test Cases
    print("Test Case 4: Exams in location range 30–50:")
    print(system.find_exams_in_range(30, 50))

    print("Test Case 5: Retrieve exam with ID 'MNO-345-678':")
    print(system.get_exam_by_id("MNO-345-678"))

    print("Test Case 6: Get another highest priority exam:")
    print(system.get_highest_priority_exam())
