use std::io::{self, Read, Write};

struct Trie {
    nxt: Vec<[u32; 26]>, // nxt[node][c] = 자식 노드 번호 (0 = 없음)
}

impl Trie {
    fn with_capacity(cap: usize) -> Self {
        let mut nxt = Vec::with_capacity(cap + 1);
        nxt.push([0u32; 26]); // 0번 = 루트
        Trie { nxt }
    }

    fn insert(&mut self, s: &[u8]) {
        let mut cur = 0usize;
        for &b in s {
            let c = (b - b'a') as usize;
            if self.nxt[cur][c] == 0 {
                self.nxt[cur][c] = self.nxt.len() as u32;
                self.nxt.push([0u32; 26]);
            }
            cur = self.nxt[cur][c] as usize;
        }
    }

    /// 루트에서 s를 끝까지 따라갈 수 있으면 S의 어떤 문자열의 접두사
    fn is_prefix(&self, s: &[u8]) -> bool {
        let mut cur = 0usize;
        for &b in s {
            let c = (b - b'a') as usize;
            match self.nxt[cur][c] {
                0 => return false,
                v => cur = v as usize,
            }
        }
        true
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();

    let n: usize = it.next().unwrap().parse().unwrap();
    let m: usize = it.next().unwrap().parse().unwrap();

    let words: Vec<&[u8]> = (0..n).map(|_| it.next().unwrap().as_bytes()).collect();
    let total: usize = words.iter().map(|w| w.len()).sum();

    // 노드 수 상한(총 길이)만큼 미리 할당 → 재할당으로 메모리가 튀지 않음
    let mut trie = Trie::with_capacity(total);
    for w in &words {
        trie.insert(w);
    }

    let ans = (0..m)
        .filter(|_| trie.is_prefix(it.next().unwrap().as_bytes()))
        .count();

    writeln!(io::stdout(), "{}", ans).unwrap();
}
