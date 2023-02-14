select * from ninjas
where id=(select max(id) from ninjas);



