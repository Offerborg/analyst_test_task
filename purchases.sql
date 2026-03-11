SELECT a.client_id
FROM account a
LEFT JOIN transaction t ON 
    a.id = t.account_id
    AND DATEDIFF(NOW(), t.transaction_date) <= 30
GROUP BY 1
HAVING COALESCE(SUM(t.amount), 0) < 5000;