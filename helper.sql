create or replace view testers_and_ratings as
select t.given, r.beer, r.score 
from taster t join ratings r on (t.id = r.taster);

create or replace view beers_and_ratings as
select r.beer, r.score 
from taster t join ratings r on (t.id = r.taster);
-- create or replace view brewers_and_ratings as

-- create or replace function avgTaster(testerName text) returns text
-- as $$ 
-- declare
--     sum         integer;
--     count       integer;
--     _exists     boolean;
--     out         text;
--     average     text;
--     r           record;
-- begin
--     select exists (select 1 from taster where given = testerName) into _exists; 
    
--     if not _exists then
--         out := 'No taster called ' || "'" || testerName || "'";
--         return out;
--     end if;

--     count := 0;
--     sum := 0;

--     for r in select * from testers_and_ratings where given = testerName
--     loop
--         count := count + 1;
--         sum := sum + r.score;
--     end loop;
    
--     average := to_char(1.0 * sum / count, '9.9');

--     out := 'Average rating for taster ' || testerName || ' is' || average;
--     return out;
-- end;
-- $$ language plpgsql;











create or replace function avgBeer(Bname text) returns text
as $$ 
declare
    count       integer := 0;
    sum         integer := 0;
    _exists     boolean;
    avg         float;
    r           record;
    beerId      int;
begin

    select exists ( select 1 from beer where name = $1) into _exists;
    
    if not exists then
        return 'No beer called ' || "'" || bname || "'";
    end if;

    select id from beer where name = Bname into beerId;

    
    for r in select * from beers_and_ratings where beer = beerId
    loop
        count := count + 1;
        sum = sum + r.score;
    end loop;

    avg = 1.0 * sum / count;

    return 'Average rating for ' || $1 || ' is' || to_char(avg, '9.9') ;

end;
$$ language plpgsql;
















create or replace function avgBrewer() returns text
as $$ 

$$ language plpgsql;
