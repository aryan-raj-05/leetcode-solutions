-- using cross join
select today.id
from weather today
cross join weather yesterday
where today.recordDate - yesterday.recordDate = 1
and today.temperature > yesterday.temperature;

-- using self join
select today.id
from weather today
join weather yesterday
on today.recordDate - yesterday.recordDate = 1
where today.temperature > yesterday.temperature;
