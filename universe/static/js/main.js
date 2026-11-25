document.addEventListener('DOMContentLoaded', () => {
    // Mobil menyu
    const toggle = document.getElementById('menuToggle');
    const links = document.getElementById('navLinks');
    if (toggle && links) toggle.addEventListener('click', () => links.classList.toggle('open'));

    // Xabarlar 4 soniyadan keyin yo'qoladi
    document.querySelectorAll('.alert').forEach((el) => {
        setTimeout(() => { el.style.opacity = '0'; setTimeout(() => el.remove(), 500); }, 4000);
    });

    // Yulduzli fon
    const sky = document.getElementById('sky');
    if (sky) {
        for (let i = 0; i < 45; i++) {
            const s = document.createElement('i');
            s.style.cssText = `left:${Math.random() * 100}%;top:${Math.random() * 100}%;animation-delay:${Math.random() * 3}s`;
            sky.appendChild(s);
        }
    }

    // Matn hisoblagichi va avtomatik balandlik
    const textarea = document.querySelector('textarea');
    const counter = document.getElementById('charCount');
    if (textarea) {
        const update = () => {
            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';
            if (counter) counter.textContent = textarea.value.length;
        };
        textarea.addEventListener('input', update);
        update();
    }

    // Bir nechta rasm: oldindan ko'rish va alohida olib tashlash
    const fileInput = document.querySelector('input[type=file][name=images]');
    const previews = document.getElementById('previews');
    if (fileInput && previews) {
        let files = [];
        const sync = () => {
            const dt = new DataTransfer();
            files.forEach((f) => dt.items.add(f));
            fileInput.files = dt.files;
            previews.innerHTML = '';
            files.forEach((f, i) => {
                const d = document.createElement('div');
                d.className = 'th';
                d.style.backgroundImage = `url(${URL.createObjectURL(f)})`;
                const x = document.createElement('b');
                x.textContent = '✕';
                x.onclick = () => { files.splice(i, 1); sync(); };
                d.appendChild(x);
                previews.appendChild(d);
            });
        };
        fileInput.addEventListener('change', () => {
            files = files.concat(Array.from(fileInput.files));
            sync();
        });
    }
});
