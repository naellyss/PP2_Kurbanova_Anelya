-- 1. Function that returns all records matching a pattern (part of name or phone number)
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p_pattern TEXT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.first_name, pb.phone
    FROM phonebook pb
    WHERE pb.first_name ILIKE '%' || p_pattern || '%'
       OR pb.phone ILIKE '%' || p_pattern || '%'
    ORDER BY pb.id;
END;
$$ LANGUAGE plpgsql;


-- 4. Function that queries data from the table with pagination (by LIMIT and OFFSET)
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.first_name, pb.phone
    FROM phonebook pb
    ORDER BY pb.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
