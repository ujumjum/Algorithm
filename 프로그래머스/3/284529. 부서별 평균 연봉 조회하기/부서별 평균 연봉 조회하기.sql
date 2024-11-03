-- 코드를 작성해주세요
select a.dept_id, a.dept_name_en, round(avg(b.sal)) as avg_sal
from hr_department a, hr_employees b
where a.dept_id = b.dept_id
group by b.dept_id
order by avg(sal) desc;