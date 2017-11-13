import json
from pyes import ES, Search
from pyes.aggs import TermsAgg, SumAgg, FilterAgg, DateHistogramAgg
from pyes.exceptions import IndexMissingException
from pyes.query import MatchAllQuery, BoolQuery, RangeQuery, ESRange, TermQuery
from pyes.filters import TermFilter, TermsFilter

match_all = MatchAllQuery()
sub_domain_agg = TermsAgg('domain_agg',
                          field='json_data.etp_domain_id',
                          size=20000)
client_agg = TermsAgg('client_agg',
                      field='json_data.etp_client_id',
                      sub_aggs=[sub_domain_agg],
                      size=20000)

search_query = Search(query=match_all, size=0)
search_query.agg.add(client_agg)

print(json.dumps(search_query.serialize(), indent=2))
