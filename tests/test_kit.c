/* Computer test for SAVE KIT's writer (src/kit_writer.h): writes a kit of 16 made-up slices (one pad left empty), then
 * tests/check_kit.py reads it back like the MPC would (gzip, header, JSON) and compares it with the template.
 *   gcc -std=gnu11 -fsanitize=address,undefined -I src tests/test_kit.c -lm -o build/test_kit && build/test_kit <dir> */
#include <ctype.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <time.h>
#include <unistd.h>
#include "kit_writer.h"

int main(int argc, char **argv) {
    const char *dir = argc > 1 ? argv[1] : "build/kits";
    float *pads[16]; long frames[16];
    for (int p = 0; p < 16; p++) {
        frames[p] = p == 5 ? 0 : 4410 + 997 * p;   /* pad 6 empty */
        pads[p] = calloc((size_t)(frames[p] ? frames[p] : 1) * 2, sizeof(float));
        for (long i = 0; i < frames[p]; i++) pads[p][2 * i] = pads[p][2 * i + 1] = 0.5f * sinf(i * 0.05f * (p + 1)) * expf(-i / 4000.0f);
    }
    char name[112], err[96];
    for (int k = 0; k < 2; k++) {   /* the second kit of the same name becomes "<name> 2" */
        if (kit_write(dir, "Funky Drummer / take \"1\" 98", 97.5, 16, pads, frames, name, sizeof name, err, sizeof err)) {
            printf("FAIL: %s\n", err); return 1;
        }
        printf("kit: %s\n", name);
    }
    /* gzip round trip of something awkward: all the same byte, then random bytes */
    size_t n = 300000; unsigned char *in = malloc(n);
    for (size_t i = 0; i < n; i++) in[i] = i < n / 2 ? 'a' : (unsigned char)(rand() & 255);
    unsigned char *gz; size_t gn;
    if (kw_gzip(in, n, &gz, &gn)) { printf("FAIL: gzip\n"); return 1; }
    char p[600]; snprintf(p, sizeof p, "%s/roundtrip.gz", dir);
    FILE *f = fopen(p, "wb"); fwrite(gz, 1, gn, f); fclose(f);
    snprintf(p, sizeof p, "%s/roundtrip.bin", dir);
    f = fopen(p, "wb"); fwrite(in, 1, n, f); fclose(f);
    for (int q = 0; q < 16; q++) free(pads[q]);
    free(gz); free(in);
    printf("ALL WRITTEN\n");
    return 0;
}
