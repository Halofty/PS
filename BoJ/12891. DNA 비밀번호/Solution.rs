use std::io::{self, Read};

fn idx(b: u8) -> usize {
    match b {
        b'A' => 0,
        b'C' => 1,
        b'G' => 2,
        _ => 3, // 'T'
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();

    let s: usize = it.next().unwrap().parse().unwrap();
    let p: usize = it.next().unwrap().parse().unwrap();
    let dna = it.next().unwrap().as_bytes();
    let need: Vec<i32> = (0..4).map(|_| it.next().unwrap().parse().unwrap()).collect();

    let mut cnt = [0i32; 4];
    let ok = |cnt: &[i32; 4]| (0..4).all(|i| cnt[i] >= need[i]);

    for &b in &dna[..p] {
        cnt[idx(b)] += 1; // 첫 윈도우
    }
    let mut ans = ok(&cnt) as u32;
    for i in p..s {
        // 한 칸씩 밀기
        cnt[idx(dna[i])] += 1;
        cnt[idx(dna[i - p])] -= 1;
        ans += ok(&cnt) as u32;
    }
    println!("{}", ans);
}