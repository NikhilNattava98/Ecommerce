CREATE TRIGGER delete_orders_trigger
BEFORE DELETE ON customers
FOR EACH ROW
BEGIN
    DELETE FROM orders WHERE customer_id = OLD.customer_id;
END;


CREATE TRIGGER delete_order_details_trigger
BEFORE DELETE ON orders
FOR EACH ROW
BEGIN
    DELETE FROM order_details WHERE order_id = OLD.order_id;
END;
