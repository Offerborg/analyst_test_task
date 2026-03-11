SELECT 
    id,
    scores,
    RANK() OVER (ORDER BY scores DESC) as position
FROM examination
ORDER BY position;