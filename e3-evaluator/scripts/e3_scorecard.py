#!/usr/bin/env python3
import os
import re
import sys
import json

def analyze_file(file_path):
    with open(file_path, 'r', errors='ignore') as f:
        content = f.read()
        lines = content.splitlines()
        
    # E3 Check detection
    e1_checks = len(re.findall(r'E1[- ]Check', content, re.IGNORECASE))
    e2_checks = len(re.findall(r'E2[- ]Check', content, re.IGNORECASE))
    e3_checks = len(re.findall(r'E3[- ]Check', content, re.IGNORECASE))
    
    # Complexity proxies
    todos = len(re.findall(r'TODO', content, re.IGNORECASE))
    long_functions = len([line for line in lines if line.strip().startswith('def ') and len(line) > 120])
    
    return {
        'e1_count': e1_checks,
        'e2_count': e2_checks,
        'e3_count': e3_checks,
        'todos': todos,
        'long_functions': long_functions,
        'line_count': len(lines)
    }

def main(dir_path):
    total_stats = {'e1': 0, 'e2': 0, 'e3': 0, 'todos': 0, 'lines': 0, 'files': 0}
    
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith(('.py', '.js', '.ts', '.md')):
                stats = analyze_file(os.path.join(root, file))
                total_stats['e1'] += stats['e1_count']
                total_stats['e2'] += stats['e2_count']
                total_stats['e3'] += stats['e3_count']
                total_stats['todos'] += stats['todos']
                total_stats['lines'] += stats['line_count']
                total_stats['files'] += 1

    # Calculation of U_E3 Score (Simplified)
    # A (Actionability) = Density of E3 Checks per 1000 lines
    a_score = min(1.0, (total_stats['e1'] + total_stats['e2'] + total_stats['e3']) / (total_stats['lines'] / 1000 + 1))
    
    # C (Completeness) = Inverse TODO density
    c_score = max(0, 1.0 - (total_stats['todos'] / (total_stats['lines'] / 100 + 1)))
    
    # L (Alignment) - Fixed for this prototype
    l_score = 0.5 
    
    final_score = 0.4 * a_score + 0.4 * l_score + 0.2 * c_score
    
    report = {
        'score': round(final_score, 2),
        'breakdown': {
            'actionability': round(a_score, 2),
            'alignment': round(l_score, 2),
            'completeness': round(c_score, 2)
        },
        'metrics': total_stats
    }
    
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    main(target_dir)
