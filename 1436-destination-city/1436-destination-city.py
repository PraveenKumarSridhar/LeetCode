class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        paths = {st:end for st,end in paths}
        
        curr_node = list(paths.keys())[0]
        
        while curr_node in paths:
            curr_node = paths[curr_node]
        
        return curr_node