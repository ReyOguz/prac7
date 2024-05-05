create or replace view testers_and_ratings as
select t.given, r.beer, r.score 
from taster t join ratings r on (t.id = r.taster);

create or replace view beers_and_ratings as
select r.beer, r.score 
from taster t join ratings r on (t.id = r.taster);

create or replace view brewers_and_ratings as
select r.beer as "Beer Id", b1.name as "Beer Name", b2.id as "Brewer ID", r.score 
from taster t 
join ratings r on (t.id = r.taster)
join beer b1 on (r.beer = b1.id)
join brewer b2 on (b1.brewer = b2.id)
;

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
        return 'No taster called ''' || testerName || ''' ';
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

    out := 'Average rating for taster ' || testerName || ' is' || average;
    return out;
end;
$$ language plpgsql;

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
    
    if not _exists then
        return 'No beer called  ''' || Bname || '''';
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
















create or replace function avgBrewer(bName text) returns text
as $$ 
declare 
    sum         integer := 0;
    count       integer := 0;
    avg         float;
    r           record;
    _exists     boolean;
    brewerId    int;
begin

    select exists( select 1 from brewer where name = bName) into _exists;

    _exists boolean;
    if not _exists then
        return 'No ratings for ' || $1;
    end if;

    select id from brewer where name = bName into brewerId;

    select exists (select 1 from brewers_and_ratings where "Brewer ID" = brewerId) into _exists;
    
    if not _exists then
        return 'No ratings for ' || $1;
    end if;

    for r in select * from brewers_and_ratings where "Brewer ID" = brewerId
    loop
        count := count + 1;
        sum := sum + r.score;
    end loop;

    if sum = 0 then
        return 'No ratings for ' || $1;
    end if;

    avg = 1.0 * sum / count;
    return 'Average rating for brewer ' || $1 || ' is ' || to_char(avg, '9.9');
end;
$$ language plpgsql;







create or replace function