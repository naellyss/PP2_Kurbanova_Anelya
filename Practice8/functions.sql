-- 1. Search contacts by pattern
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p TEXT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.first_name, phonebook.phone
    FROM phonebook
    WHERE phonebook.first_name ILIKE '%' || p || '%'
       OR phonebook.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


-- 4. Get contacts with pagination
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.first_name, phonebook.phone
    FROM phonebook
    ORDER BY phonebook.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
