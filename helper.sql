create or replace view testers_and_ratings as
select t.given, r.beer, r.score 
from taster t join ratings r on (t.id = r.taster);

-- create or replace view brewers_and_ratings as
-- create or replace view beers_and_ratings as

create or replace function avgTaster(testerName text) returns text
as $$ 
declare
    sum         integer;
    count       integer;
    _exists     boolean;
    out         text;
    average     text;
    r           record;
begin
    select exists (select 1 from taster where given = testerName) into _exists; 
    
    if not _exists then
        out := 'No taster called ' || "'" || testerName || "'";
        return out;
    end if;

    count := 0;
    sum := 0;

    for r in select * from testers_and_ratings where given = testerName
    loop
        count := count + 1;
        sum := sum + r.score;
    end loop;
    
    average := to_char(1.0 * sum / count, '9.9');

    out := 'Average rating for taster ' || testerName || ' is ' || average;
    return out;
end;
$$ language plpgsql;



create or replace function avgBrewer() returns text
as $$ 

$$ language plpgsql;




create or replace function avgbeer() returns text
as $$ 

$$ language plpgsql;
