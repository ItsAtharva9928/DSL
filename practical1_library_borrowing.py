from collections import Counter

borrow_counts = [2, 0, 3, 5, 0, 2]

book_borrow_counts = {
    "Book1": 4,
    "Book2": 1,
    "Book3": 7
}

# Average number of books borrowed
avg = sum(borrow_counts) / len(borrow_counts)
print("Average borrowing:", avg)

# Highest and lowest borrowed books
highest = max(book_borrow_counts, key=book_borrow_counts.get)
lowest = min(book_borrow_counts, key=book_borrow_counts.get)

print("Highest borrowed book:", highest)
print("Lowest borrowed book:", lowest)

# Count members who borrowed zero books
zero_count = borrow_counts.count(0)
print("Members with zero borrowing:", zero_count)

# Find mode of book borrowing counts
freq = Counter(book_borrow_counts.values())
mode = freq.most_common(1)[0][0]

print("Mode of borrowing counts:", mode)
