-- Active: 1697165492442@@127.0.0.1@3306@library
use library;

SELECT * FROM books;

ALTER TABLE books
DROP PRIMARY KEY;

ALTER TABLE books
ADD PRIMARY KEY (book_id);

SELECT book_id, COUNT(*)
FROM books
GROUP BY book_id
HAVING COUNT(*) > 1;

SELECT title FROM book_content WHERE chapter_id = 10;

ALTER TABLE book_content ADD COLUMN chapter_id INT;


SET @row_number = 0;
UPDATE book_content
SET chapter_id = @row_number := @row_number + 1
ORDER BY title;

ALTER TABLE books
ADD PRIMARY KEY (book_id);


UPDATE book_content SET book_name = NULL;

SELECT DISTINCT book_name FROM book_content;

SELECT * FROM books;

SELECT * FROM book_content WHERE book_name = '水浒传';

SELECT DISTINCT book_name FROM book_content;

DELETE FROM books;

INSERT INTO books (book_id, book_name, author, tag) VALUES (1, '红楼梦', '曹雪芹', '国学经典');
INSERT INTO books (book_id, book_name, author, tag) VALUES (2, '水浒传', '施耐庵', '国学经典');
INSERT INTO books (book_id, book_name, author, tag) VALUES (3, '三国演义', '罗贯中', '国学经典');
SELECT title, content FROM book_content WHERE chapter_id = 22923;
SELECT title, chapter_id FROM book_content
JOIN books ON book_content.book_name=books.book_name
WHERE book_id = 3;

SELECT book_name FROM books WHERE book_id = 3;

SELECT book_id FROM books 
JOIN book_content ON books.book_name = book_content.book_name
WHERE chapter_id = 3;

SELECT title, chapter_id, chapter_num FROM book_content JOIN books ON book_content.book_name=books.book_name WHERE book_id = 2 ORDER BY chapter_num ASC;

SELECT book_name, title, content, chapter_num FROM book_content
WHERE chapter_num = '1';
SELECT chapter_id FROM book_content WHERE chapter_num = '2' AND book_name = '狂仙';

SELECT title, chapter_num FROM book_content JOIN books ON book_content.book_name=books.book_name WHERE book_id = 2 ORDER BY chapter_num ASC;

SELECT chapter_id FROM book_content WHERE title = '楔子 张天师祈禳瘟疫 洪太尉误走妖魔';

SELECT MAX(chapter_num) FROM book_content JOIN books ON books.book_name = book_content.book_name WHERE book_id = 2;
SELECT title, content, chapter_num, book_name FROM book_content WHERE chapter_id = '23253';

SELECT MAX(chapter_num) FROM book_content
JOIN books ON books.book_name=book_content.book_name
WHERE books.book_name = '红楼梦';