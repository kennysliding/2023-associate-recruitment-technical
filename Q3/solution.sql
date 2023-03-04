SELECT o.owner_id, o.owner_name, COUNT(DISTINCT ac.category_id) AS different_category_count 
FROM owner o 
    JOIN article a ON o.owner_id = a.owner_id 
    JOIN article_category ac ON a.article_id = ac.article_id 
GROUP BY o.owner_id, o.owner_name 
ORDER BY different_category_count DESC;